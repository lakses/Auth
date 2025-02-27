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
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(1209600)  # 2 недели
            return redirect('home')  
        else:
            return render(request, 'login.html', {'error': 'Неверные учетные данные.'})
    return render(request, 'login.html')


def home(request):
    user = request.user
    return render(request, 'account.html', {
        'username': user.username,
        'email': user.email,
        'password_display': '*' * 8
    })
