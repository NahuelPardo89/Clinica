from django.contrib import admin
from .models import Consulta, Especialidad, Medico, MedicoHasEspecialidad, Obrasocial, ObrasocialHasMedico,ObrasocialHasPaciente,Paciente,Turno 

# Register your models here.
admin.site.register(Consulta)
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(MedicoHasEspecialidad)
admin.site.register(Obrasocial)
admin.site.register(ObrasocialHasMedico)
admin.site.register(ObrasocialHasPaciente)
admin.site.register(Paciente)
admin.site.register(Turno)