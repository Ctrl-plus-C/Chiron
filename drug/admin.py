from django.contrib import admin
from .models import Nutrient, HeartRate, Symptomrecord, Diseaserecord, Record, Foodlist, Foodrecord

# Register your models here.
admin.site.register(Nutrient)
admin.site.register(HeartRate)
admin.site.register(Symptomrecord)
admin.site.register(Diseaserecord)
admin.site.register(Record)
admin.site.register(Foodrecord)
admin.site.register(Foodlist)