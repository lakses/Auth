from django.contrib import admin
from django.urls import path, include
from .views import main, create_news, news_detail
from django.conf.urls.static import static
urlpatterns = [
    path('',main,name='main_page'),
    path('create-news/', create_news, name='create_news'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),

]
