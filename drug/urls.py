from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'api/login', views.login, name='login'),
    url(r'api/sampleapi', views.sample_api, name='sample_api'),
]
