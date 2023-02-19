from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model= Paciente
        fields='__all__'
        
class formBuscarPaciente(forms.Form):
    dni = forms.CharField(label='DNI', max_length=8)