from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/paciente/index.html')

def paciente(request):
    pacientes= Paciente.objects.all()
    return render(request, 'paginas/paciente/listaPaciente.html',{'pacientes':pacientes})

def formRegistroPaciente(request):
    formulario= PacienteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('paciente')
    return render(request, 'paginas/paciente/formRegistroPaciente.html',{'formulario':formulario})

def formEditPaciente(request):
    return render(request, 'paginas/paciente/formEditPaciente.html')

def borrarPaciente(request, dni):
    paciente=Paciente.objects.get(dni=dni)
    paciente.delete()
    return redirect('paciente')
