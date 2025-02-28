from django.contrib import admin
from django.urls import path, include
from .views import main,create_news
from django.conf.urls.static import static
urlpatterns = [
    path('',main,name='main-page'),
    path('create-news/', create_news, name='create_news'),
]
