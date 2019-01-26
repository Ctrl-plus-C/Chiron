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