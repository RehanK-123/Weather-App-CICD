from django.urls import path
from app import views

urlpatterns = [path('', views.home, name= 'home'),
               path('weather', views.weather, name= 'weather'),]