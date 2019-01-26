from django.contrib import admin
from .models import Nutrient
from .models import HeartRate

# Register your models here.
admin.site.register(Nutrient)
admin.site.register(HeartRate)