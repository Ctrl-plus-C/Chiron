from django.contrib import admin
from .models import Nutrient, HeartRate

# Register your models here.
admin.site.register(Nutrient)
admin.site.register(HeartRate)