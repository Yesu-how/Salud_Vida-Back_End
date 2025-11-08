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