from django.contrib import admin
from .models import Nutrient, HeartRate, Symptomrecord, Diseaserecord, Record

# Register your models here.
admin.site.register(Nutrient)
admin.site.register(HeartRate)
admin.site.register(Symptomrecord)
admin.site.register(Diseaserecord)
admin.site.register(Record)