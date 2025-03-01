from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register,home,login_view,change_pass,change_email

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/',home, name = 'home'),
    path('change-password/',change_pass, name = 'change_pass'),
    path('change-email/', change_email, name='change_email'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
