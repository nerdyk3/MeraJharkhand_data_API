from django.contrib import admin
from django.urls import path
from . import views

app_name = 'MJ_data'

urlpatterns = [
    path('index/', views.index, name='index'),
    
]