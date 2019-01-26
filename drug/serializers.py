from rest_framework import serializers
from .models import Nutrient, Selfcarediary
from .models import HeartRate


class NutrientsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Nutrient
        fields = ('meal', 'date','user')

class HeartRateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = HeartRate
        fields = ('bpm', 'date','user')

class SelfcarediarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Selfcarediary
        fields = ('user', 'date', 'diary')