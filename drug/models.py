from django.db import models

# Create your models here.
class Nutrient(models.Model):
    glasses_water = models.IntegerField()
    meal = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.date)

    def __unicode__(self):
        return str(self.date)

class HeartRate(models.Model):
    bpm = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.date)

    def __unicode__(self):
        return str(self.date)