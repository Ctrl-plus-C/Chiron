from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'api/login', views.login, name='login'),
    url(r'api/sampleapi', views.sample_api, name='sample_api'),
    url(r'api/nutrient',views.NutrientsApi.as_view() ,name='Nutrient'),
    url(r'api/heart_rate',views.HeartRateApi.as_view() ,name='Heart Rate'),
    url(r'api/parse', views.ParseD.as_view(), name='gete'),
    url(r'api/condition', views.Condition.as_view(), name='gete'),
    url(r'api/symptom', views.Symptom.as_view(), name='gete'),
    url(r'api/diagonisis', views.Diagnosis.as_view(), name='gete'),
    url(r'^login/$', views.loginpage, name="loginpage"),
]
