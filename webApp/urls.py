from django.urls import path
from .views import  registro
from .views import home
from .views import index
from .views import cerrarSession, iniciarSesion
from .views import productos
from .views import dashboard

urlpatterns = [
    path('',home, name='home'),

    path('home/',home, name='home'),
    
    path('registro/',registro, name='registro' ),

    path('index/',index, name='index'),

    path('cerrarSesion/',cerrarSession, name='CS'),

    path('iniciarSesion/',iniciarSesion, name='IS'),
    
    path('productos/',productos, name='productos'),

    path('dashboard/',dashboard, name='dashboard'),

   
]
