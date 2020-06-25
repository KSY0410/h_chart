from django.contrib import admin
from django.urls import path
from covid import views
urlpatterns = [
    path('', views.covid, name='covid')]