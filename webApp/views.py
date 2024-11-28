from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import models
from django.contrib.auth.decorators import login_required
from .models import  Productos, Categoria, Orden


def home (request):
    return render (request, 'webApp/home.html')


def registro(request):
    if request.method =='GET':
         return render (request, 'webApp/registro.html', {
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST ['password2']:

          try:
            user= User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('dashboard')
          except:
            
            return render (request, 'webApp/registro.html', {
                'form': UserCreationForm,
                "error":'El usuario ya existe'
    })        
        
        return render (request, 'webApp/registro.html', {
                'form': UserCreationForm,
                "error":'Las contraseñas no coinciden'
    })   



def index(request):
   return render(request, 'webApp/index.html')


def cerrarSession(request):
   logout(request)
   return redirect('home')


def iniciarSesion(request):
  if request.method == 'GET':
     return render(request, 'webApp/iniciarSesion.html',{
        'form' : AuthenticationForm
     })
  else:
       user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
       if user is None:
           return render(request, 'webApp/iniciarSesion.html',{
        'form' : AuthenticationForm,
        'error': 'Usuario o Contraseña es incorreta'
     })
       else:
          login(request,user)
          return redirect('dashboard')
       
@login_required      
def productos (request):
    return render (request, 'webApp/productos.html')

@login_required
def dashboard(request):
    # Obtener información para mostrar en el dashboard
   return render (request, 'webApp/dashboard.html')

