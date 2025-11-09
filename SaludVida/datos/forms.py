from django import forms
from .models import Paciente, Medico, Cita
import re

patron = r"^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$"

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["nombre_completo", "rut", "fecha_nacimiento", "sexo", "telefono"]
        widgets = {
            "nombre_completo": forms.TextInput(attrs={"class": "form-control", "placeholder": "ingrese nombre y apellido"}),
            "rut": forms.TextInput(attrs={"class": "form-control", "placeholder": "ej 12.345.678-9"}),
            "sexo": forms.Select(attrs={"class":"form-control", "placeholder": "Sexo"}),
            "fecha_nacimiento": forms.DateInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "placeholder": "ej: +56912345678"})
        }

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if len(nombre.split()) < 2:
            raise forms.ValidationError("Debe de colocar como mínimo un nombre y un apellido")
        

        if not re.fullmatch(patron, nombre):
            raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
        