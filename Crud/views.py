from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm
from .forms import formBuscarPaciente

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

def formEditPaciente(request,dni):
    paciente = Paciente.objects.get(dni=dni)
    formulario = PacienteForm(request.POST or None, request.FILES or None, instance= paciente) 
    if formulario.is_valid():
        formulario.save()
        return redirect('paciente')
    return render(request, 'paginas/paciente/formRegistroPaciente.html', {'formulario': formulario})

def borrarPaciente(request, dni):
    paciente=Paciente.objects.get(dni=dni)
    paciente.delete()
    return redirect('paciente')



def buscarPaciente(request):
    formulario = formBuscarPaciente(request.GET or None)
    pacientes = []
    if formulario.is_valid():
        dni = formulario.cleaned_data.get('dni')
        pacientes = Paciente.objects.filter(dni=dni)
    return render(request, 'paginas/paciente/buscarPaciente.html', {'formulario': formulario, 'pacientes': pacientes})