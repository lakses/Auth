from django.contrib import admin
from django.urls import path, include
from .views import main
from accounts.urls import home

urlpatterns = [
    path('',main,name='main-page')
]
