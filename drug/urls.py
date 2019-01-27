from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'api/nutrient',views.NutrientsApi.as_view() ,name='Nutrient'),
    url(r'^selfdiary/$', views.selfdiary, name="selfdiarya"),
    url(r'api/heart_rate',views.HeartRateApi.as_view() ,name='Heart Rate'),
    url(r'api/parse', views.ParseD.as_view(), name='parse'),
    url(r'api/condition', views.Condition.as_view(), name='condition'),
    url(r'api/symptom', views.Symptom.as_view(), name='symptom'),
    url(r'api/diagnose', views.Diagnosis.as_view(), name='diagnose'),
    url(r'^medication/$', views.medication, name="medication"),
    url(r'^nutrients/$', views.nutrients, name="nutrients"),
    url(r'api/prescription', views.Prescription.as_view(), name='prescription'),
    url(r'^login/$', views.loginpage, name="loginpage"),
    url(r'api/selfdiary', views.SelfdiaryApi.as_view(), name='selfdiary'),
    url(r'^analytics/$', views.analytics, name="analytics"),
]
