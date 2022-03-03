from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('bedAvailablity/',views.bedAvailablity,name = 'bedAvailablity'),
    path('staffDashboard/',views.staffDashboard,name='staffDashboard'),
    path('index/',views.home,name='index'),
]
