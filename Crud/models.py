from django.db import models

# Create your models here.
class Consulta(models.Model):
    idconsulta = models.IntegerField(db_column='idConsulta', primary_key=True)  # Field name made lowercase.
    costo = models.IntegerField()
    medico_dni = models.ForeignKey('Medico', models.DO_NOTHING, db_column='Medico_dni')  # Field name made lowercase.
    turno_idturno = models.ForeignKey('Turno', models.DO_NOTHING, db_column='turno_idturno')

    def __str__(self):
        return self.idconsulta


class Especialidad(models.Model):
    idespecialidad = models.IntegerField(db_column='idEspecialidad', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)

    


class Medico(models.Model):
    dni = models.IntegerField(primary_key=True)
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)

    

class MedicoHasEspecialidad(models.Model):
    medico_dni = models.OneToOneField(Medico, models.DO_NOTHING, db_column='Medico_dni', primary_key=True)  # Field name made lowercase.
    especialidad_idespecialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='Especialidad_idEspecialidad')  # Field name made lowercase.

    


class Obrasocial(models.Model):
    idobrasocial = models.IntegerField(db_column='idobraSocial', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)

    


class ObrasocialHasMedico(models.Model):
    obrasocial_idobrasocial = models.OneToOneField(Obrasocial, models.DO_NOTHING, db_column='obraSocial_idobraSocial', primary_key=True)  # Field name made lowercase.
    medico_dni = models.ForeignKey(Medico, models.DO_NOTHING, db_column='Medico_dni')  # Field name made lowercase.

    


class ObrasocialHasPaciente(models.Model):
    obrasocial_idobrasocial = models.OneToOneField(Obrasocial, models.DO_NOTHING, db_column='obraSocial_idobraSocial', primary_key=True)  # Field name made lowercase.
    paciente_dni = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='Paciente_dni')  # Field name made lowercase.

    


class Paciente(models.Model):
    dni = models.IntegerField(primary_key=True)
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.EmailField( blank=True, null=True)
    contrasena = models.CharField(max_length=45)
    userinstagram = models.CharField(db_column='userInstagram', max_length=60, blank=True, null=True)  # Field name made lowercase.
    userfacebook = models.CharField(max_length=60, blank=True, null=True)

    


class Turno(models.Model):
    idturno = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    paciente_dni = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='Paciente_dni')  # Field name made lowercase.

    