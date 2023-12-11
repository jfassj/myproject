# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    else:
        return render(request, 'login.html')

@login_required
def home(request):
    users = UserProfile.objects.all()
    return render(request, 'home.html', {'users': users})

def user_logout(request):
    logout(request)
    return redirect('/login/')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        # Crear un nuevo usuario y perfil
        user = User.objects.create(username=username, email=email, password=make_password(password))
        UserProfile.objects.create(username=username, email=email, password=make_password(password))

        # Iniciar sesión automáticamente después del registro
        login(request, user)
        
        return redirect('/home/')
    else:
        return render(request, 'register.html')
