from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('formEditPaciente', views.formEditPaciente, name='formEditPaciente'),
    path('formRegistroPaciente', views.formRegistroPaciente, name='formRegistroPaciente'),
    path('paciente', views.paciente, name='paciente'),
    path('borrarPaciente/<int:dni>', views.borrarPaciente, name='borrarPaciente'),
    path('formEditPaciente/<int:dni>', views.formEditPaciente, name='formEditPaciente'),
]