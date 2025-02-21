from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .Form import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрированы и вошли в систему.')
            return redirect('home') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            messages.success(request, 'Вы успешно вошли в систему.')
            return redirect('home')  
        else:
            messages.error(request, 'Неверный логин или пароль.')

    return render(request, 'login.html')  

def home(request):
    return HttpResponse('<h1>Круто</h1>') 
