from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .Form import RegistrationForm
from django.contrib.auth.models import User

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

@login_required
def home(request):
    user = request.user
    return render(request, 'account.html', {
        'username': user.username,
        'email': user.email,
        'password_display': '*' * 8
    })

@login_required
def change_pass(request):
     if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = request.user

        if not user.check_password(old_password):
            messages.error(request, 'Старый пароль неверный.')
            return render(request, 'change_password.html')

        if new_password != confirm_password:
            messages.error(request, 'Новые пароли не совпадают.')
            return render(request, 'change_password.html')

        user.set_password(new_password)
        user.save()

        update_session_auth_hash(request, user)

        messages.success(request, 'Пароль успешно изменен.')
        return redirect('home')
     return render(request, 'change_pass.html')

def change_email(request):
    if request.method == 'POST':
        password = request.POST['password']
        new_email = request.POST['new_email']
        
        user = request.user

        # Проверка правильности пароля
        if not user.check_password(password):
            messages.error(request, 'Пароль неверный.')
            return render(request, 'change_email.html')

        # Проверка на уникальность нового email
        if User.objects.filter(email=new_email).exists():
            messages.error(request, 'Этот адрес электронной почты уже используется.')
            return render(request, 'change_email.html')

        # Изменение email
        user.email = new_email
        user.save()

        messages.success(request, 'Адрес электронной почты успешно изменен.')
        return redirect('home')

    return render(request, 'change_email.html')