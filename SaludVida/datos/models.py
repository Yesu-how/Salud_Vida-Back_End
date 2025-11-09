from django.db import models

# Create your models here.
class Medico(models.Model):
    nombre_completo = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    especialidad = models.CharField(max_length=20)
    correo = models.EmailField(max_length=25, unique=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre_completo
    
    class Meta:
        ordering = ["nombre_completo"]
        verbose_name = "Médico"

class Paciente(models.Model):
    Opciones_Sexo = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
    nombre_completo = models.CharField(max_length=50)
    rut = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=Opciones_Sexo)
    telefono = models.CharField(null=True, blank=True, max_length=12)

    def __str__(self) -> str:
        return self.nombre_completo
    
    class Meta:
        ordering = ["nombre_completo"]

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, related_name= "citas_P", on_delete=models.CASCADE )
    medico = models.ForeignKey(Medico, related_name= "consultas_M", on_delete=models.CASCADE )
    especialidad = models.CharField(max_length=50)
    fecha_cita = models.DateField(auto_now=True)
    hora_cita = models.TimeField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.hora_cita
    
    class Meta:
        ordering = ["fecha_cita", "hora_cita"]
        unique_together = ('fecha_cita', 'hora_cita', 'fecha_cita')