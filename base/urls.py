from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('tests/',views.tests,name='tests')
    
]
