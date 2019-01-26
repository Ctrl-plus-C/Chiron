from rest_framework import serializers
from .models import Nutrient
from .models import HeartRate
import logging

logger = logging.getLogger('django')

class NutrientsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Nutrient
        fields = ('glasses_water', 'meal', 'date')

class HeartRateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = HeartRate
        fields = ('bpm', 'date')