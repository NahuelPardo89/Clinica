from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('formEditPaciente', views.formEditPaciente, name='formEditPaciente'),
    path('formRegistroPaciente', views.formRegistroPaciente, name='formRegistroPaciente'),
    

]