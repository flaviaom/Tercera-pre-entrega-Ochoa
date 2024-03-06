from django.urls import path
from AppSalud.views import *

urlpatterns = [

    path('', inicio, name = 'Home'),
    path('crear_usuario/', crear_paciente, name = 'newuser'),
    path('crear_doctor/', crear_doctor, name = 'newdoc'),
    path('agendar_cita/', agendar_cita, name = 'newcita'),
    path('buscar_cita/', buscar_cita, name = 'buscarcita'),

]