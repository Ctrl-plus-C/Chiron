from django.shortcuts import render
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


def search(symptom):
        api = infermedica_api.get_api()
        data = api.search(symptom["orth"])
        return data

class ParseD(APIView):
    def post(self,request):
        sentence = request.data.get("text")
        api = infermedica_api.get_api()
        response = api.parse(sentence).to_dict()["mentions"]
        # import pdb; pdb.set_trace()
        mysymptomlist = {}
        for data in response:
            mysymptomlist["orth"] = data["orth"]
            mysymptomlist["id"] = data["id"]
        
        # import pdb; pdb.set_trace()
        callsearchdata = api.search(mysymptomlist)
        
        return Response(callsearchdata, status=status.HTTP_200_OK)

class Condition(APIView):
    def post(self, request):
        api = infermedica_api.API(app_id='945555e1', app_key='be2ee424c225c567086a084637a359de')
        # r = infermedica_api.Diagnosis(app_id='945555e1', app_key='be2ee424c225c567086a084637a359de')
        data = api.conditions_list()
        
        # r = requests.post(url, data=json.dumps({'text': text}),headers={'Authorization': apiKey, 'Content-Type': 'application/json'})
        return Response({"test":data}, status=status.HTTP_200_OK)

# class Search(APIView):

class Diagnosis(APIView):
    def post(self,request):
        orth = request.data.get("orth")
        s_id = request.data.get("id")
        api = infermedica_api.get_api()
        re = infermedica_api.Diagnosis(sex=request.data.get("sex"), age=request.data.get("age"))
        
        # import pdb; pdb.set_trace()
        re.add_symptom(s_id, 'present', initial=True)
        # re.add_symptom('s_98', 'present', initial=True)
        # re.add_symptom('s_107', 'absent')

        re= api.diagnosis(re).to_dict()
        import pdb; pdb.set_trace()
        return Response({"test":re["conditions"]}, status=status.HTTP_200_OK)
        
    # call diagnosis
        

class Symptom(APIView):
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

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, restdetails = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, "hasuraid": user.id},
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

class HeartRateApi(APIView):
    def get(self, request):
        logger.info('Get request initiated.')
        try:
            nutrients = Nutrient.objects.all()
            nserializer = NutrientsSerializer(nutrients)
            nutrient_data = nserializer.data
            logger.info("Request completed\nRequest status code: 200\nData: " + str(nutrient_data))
            return Response(booking_data, status=status.HTTP_200_OK)
        except:
            logger.error('No details found for given date')
            return Response({'success': False, 'message': 'No details found for given date'}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        logger.info('Update request initiated.')
        request_data = request.data.copy()
        request_data['date'] = datebooking
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
            logger.info('Request completed\nRequest status code: 200\nData: ' + str(bserializer.data))
            return Response(bserializer.data, status=status.HTTP_200_OK)
        logger.error(bserializer.errors)
        return Response(bserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NutrientsApi(APIView):
    def get(self, request):
        logger.info('Get request initiated.')
        try:
            nutrients = Nutrient.objects.all()
            nserializer = NutrientsSerializer(nutrients)
            nutrient_data = nserializer.data
            logger.info("Request completed\nRequest status code: 200\nData: " + str(nutrient_data))
            return Response(booking_data, status=status.HTTP_200_OK)
        except:
            logger.error('No details found for given date')
            return Response({'success': False, 'message': 'No details found for given date'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        logger.info('Update request initiated.')
        request_data = request.data.copy()
        request_data['date'] = datebooking
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
            logger.info('Request completed\nRequest status code: 200\nData: ' + str(bserializer.data))
            return Response(bserializer.data, status=status.HTTP_200_OK)
        logger.error(bserializer.errors)
        return Response(bserializer.errors, status=status.HTTP_400_BAD_REQUEST)
