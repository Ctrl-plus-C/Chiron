from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Nutrient
from .serializers import NutrientsSerializer
from rest_framework.views import APIView
from rest_framework import permissions, status
import infermedica_api
# import Symp

import requests,json
infermedica_api.configure(app_id='945555e1', app_key='be2ee424c225c567086a084637a359de')

def home(request):
    if request.user.is_authenticated():
        return render(request, 'drug/home.html',{})
    return redirect('accounts/login')

def loginpage(request):
    return render(request, 'drug/login.html', {})

def search(symptom):
        import pdb; pdb.set_trace()
        api = infermedica_api.get_api()
        data = api.search(symptom["orth"])
        return data

class Prescription(APIView):
    @csrf_exempt
    def post(self,request):
        medicname = request.data.get("text")
        # import pdb; pdb.set_trace()
        data = requests.get("https://api.fda.gov/drug/label.json?search="+medicname).json()
        
        return Response(data, status=status.HTTP_200_OK)

def medication(request):
    if request.user.is_authenticated():
        return render(request, 'drug/medication.html', {})
    return redirect('accounts/login.html')

class ParseD(APIView):
    @csrf_exempt
    def post(self,request):
        sentence = request.data.get("text")
        api = infermedica_api.get_api()
        response = api.parse(sentence).to_dict()["mentions"]
        mysymptomlist = []
        templist = {}
        print("reached templist")
        for data in response:
            templist["orth"] = data["orth"]
            templist["id"] = data["id"]
            mysymptomlist.append(templist.copy())

        finalsearchdata = []
        print("reached finalserach")
        for symptom in mysymptomlist:
            callsearchdata = api.search(symptom['orth'])
            finalsearchdata.extend(callsearchdata)
        finaldict = {}
        print("conversion")
        for dictdata in finalsearchdata:
            finaldict[dictdata['label']] = dictdata['id']

        return Response(finaldict, status=status.HTTP_200_OK)

class Condition(APIView):
    @csrf_exempt
    def post(self, request):
        api = infermedica_api.API(app_id='945555e1', app_key='be2ee424c225c567086a084637a359de')
        # r = infermedica_api.Diagnosis(app_id='945555e1', app_key='be2ee424c225c567086a084637a359de')
        data = api.conditions_list()
        
        # r = requests.post(url, data=json.dumps({'text': text}),headers={'Authorization': apiKey, 'Content-Type': 'application/json'})
        return Response({"test":data}, status=status.HTTP_200_OK)

# class Search(APIView):


class Diagnosis(APIView):
    @csrf_exempt
    def post(self,request):
        present_symptoms = request.data.getlist('choices[]')
        absent_symptoms = request.data.getlist('unchoices[]')
        api = infermedica_api.get_api()
        re = infermedica_api.Diagnosis(sex=request.data.get("gender"), age=request.data.get("age"))

        for symptom in present_symptoms:            
            re.add_symptom(symptom, 'present')
        for symptom in absent_symptoms:
            re.add_symptom(symptom, 'absent')

        re= api.diagnosis(re).to_dict()
        return Response({"test":re}, status=status.HTTP_200_OK)
        
    # call diagnosis
        

class Symptom(APIView):
    @csrf_exempt
    def post(self,request):
        api = infermedica_api.get_api()
        
        response = api.parse(sentence).to_dict()["mentions"]
        # import pdb; pdb.set_trace()
        mysymptomlist = {}
        for data in response:
            mysymptomlist["orth"] = data["orth"]
            mysymptomlist["id"] = data["id"]
            data.append(api.symptom_details(mysymptomlist["id"]))
            
        return Response({"test":data},status=status.HTTP_200_OK)



# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, restdetails = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key, "hasuraid": user.id},
#                     status=HTTP_200_OK)

# @csrf_exempt
# @api_view(["GET"])
# def sample_api(request):
#     data = {'sample_data': 123}
#     return Response(data, status=HTTP_200_OK)


class HeartRateApi(APIView):
    @csrf_exempt
    def get(self, request):
        try:
            heartrate = HeartRate.objects.all()
            hserializer = HeartRateSerializer(heartrate)
            heartrate_data = hserializer.data
            return Response(heartrate_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No details found for given date'}, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    def post(self, request, user):
        request_data = request.data.copy()
        request_data['user'] = user
        singleroomaval = request_data.get('singleroomaval','')
        doubleroomaval = request_data.get('doubleroomaval','')
        if singleroomaval != '':
            if int(singleroomaval) > 5 or int(singleroomaval) < 0:
                return Response({"success": False,"message": "Availability must be between 0 and 5."}, status=status.HTTP_400_BAD_REQUEST)
        if doubleroomaval != '':
            if int(doubleroomaval) > 5 or int(doubleroomaval) < 0:
                return Response({"success": False,"message": "Availability must be between 0 and 5."}, status=status.HTTP_400_BAD_REQUEST)                
        try:
            booking = Booking.objects.get(date=datebooking)
            bserializer = BookingSerializer(booking, data=request_data, partial=True)
        except:
            bserializer = BookingSerializer(data=request_data)
        if bserializer.is_valid():
            bserializer.save()
            return Response(bserializer.data, status=status.HTTP_200_OK)
        return Response(bserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NutrientsApi(APIView):
    @csrf_exempt
    def get(self, request):
        try:
            nutrients = Nutrient.objects.all()
            nserializer = NutrientsSerializer(nutrients)
            nutrient_data = nserializer.data
            return Response(nutrient_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No details found for given date'}, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    def post(self, request):
        request_data = request.data.copy()
        request_data["user"] = request.user.pk
        mealval = request_data.get('meal','')
        data = {
            "query":mealval,
            "timezone": "US/Eastern"
            }
        result = requests.post('https://trackapi.nutritionix.com/v2/natural/nutrients', data, headers={"x-app-id":"94f5edb6","x-app-key":"8bb3ae712275e9810ceec3b583e2727d"})
        calories = 0
        fat = 0
        sugar = 0
        protein = 0
        carbs = 0
        vita = 0
        vitb = 0
        vitc = 0
        vitd = 0
        vite = 0
        foodlist = ""
        for fooditem in result.json()["foods"]:
            foodlist += fooditem["food_name"]+"; "
            calories+=fooditem["nf_calories"]
            fat+=fooditem["nf_total_fat"]
            sugar+=fooditem["nf_sugars"]
            protein+=fooditem["nf_protein"]
            carbs+=fooditem["nf_total_carbohydrate"]
            nutlist = fooditem["full_nutrients"] 
            vita+=nutlist[22]["value"]+nutlist[24]["value"]
            vitb+=nutlist[38]["value"]+nutlist[40]["value"]
            vitc+=nutlist[33]["value"]
            vitd+=nutlist[29]["value"]
            vite+=nutlist[27]["value"]

        response = {
            "Food List":foodlist,
            "Calories":calories,
            "Fat":fat,
            "Sugars":sugar,
            "Protein":protein,
            "Carbohydrates":carbs,
            "Vitamin A":vita,
            "Vitamin B Complex":vitb,
            "Vitamin C":vitc,
            "Vitamin D":vitd,
            "Vitamin E":vite
        }

        nserializer = NutrientsSerializer(data=request.data)
        if nserializer.is_valid():
            nserializer.save()
            return Response(response, status=status.HTTP_200_OK)
        return Response(nserializer.errors, status=status.HTTP_400_BAD_REQUEST)
