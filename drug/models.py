from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Nutrient(models.Model):
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
        return self.user.username

    def __unicode__(self):
        return self.user.username

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    search_query = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Symptomrecord(models.Model):
    user_record = models.ForeignKey(Record, on_delete=models.CASCADE,blank=True,null=True)
    present_symptoms = models.CharField(max_length=1000,blank=True,null=True)
    present_symptoms_id = models.CharField(max_length=1000, blank=True,null=True)

    def __str__(self):
        return self.user_record.user.username

    def __unicode__(self):
        return self.user_record.user.username

class Diseaserecord(models.Model):
    user_record = models.ForeignKey(Record, on_delete=models.CASCADE,blank=True,null=True)
    probable_diseases = models.CharField(max_length=1000,blank=True,null=True)
    probable_diseases_id = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return self.user_record.user.username

    def __unicode__(self):
        return self.user_record.user.username

class Foodrecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    search_query = models.CharField(max_length=1000, blank=True, null=True)
    calories = models.DecimalField(max_digits=19, decimal_places=10)
    fat = models.DecimalField(max_digits=19, decimal_places=10)
    sugars = models.DecimalField(max_digits=19, decimal_places=10)
    protein = models.DecimalField(max_digits=19, decimal_places=10)
    carbohydrates = models.DecimalField(max_digits=19, decimal_places=10)
    vitamina = models.DecimalField(max_digits=19, decimal_places=10)
    vitaminbcomplex = models.DecimalField(max_digits=19, decimal_places=10)
    vitaminc = models.DecimalField(max_digits=19, decimal_places=10)
    vitamind = models.DecimalField(max_digits=19, decimal_places=10)
    vitamine = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

class Foodlist(models.Model):
    food_record = models.ForeignKey(Foodrecord, on_delete=models.CASCADE, blank=True, null=True)
    food_item = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.food_record.user.username

    def __unicode__(self):
        return self.food_record.user.username