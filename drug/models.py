from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Nutrient(models.Model):
    glasses_water = models.IntegerField()
    meal = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return str(self.date)

    def __unicode__(self):
        return str(self.date)

class HeartRate(models.Model):
    bpm = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.date)

    def __unicode__(self):
        return str(self.date)