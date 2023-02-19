from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'paginas/paciente/index.html')

def formRegistroPaciente(request):
    return render(request, 'paginas/paciente/formRegistroPaciente.html')

def formEditPaciente(request):
    return render(request, 'paginas/paciente/formEditPaciente.html')

