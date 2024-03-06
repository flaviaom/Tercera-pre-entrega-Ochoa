from django import forms
from AppSalud.models import *

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField()
    direccion = forms.CharField()
    telefono = forms.CharField(max_length=15)


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'especialidad', 'telefono', 'correo']

    especialidad = forms.ChoiceField(choices=Doctor.opciones_especialidad, widget=forms.Select(attrs={'class': 'form-control'}))


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

    widgets = {
        'fecha': forms.TextInput(attrs={'type': 'datetime-local'}),
    }