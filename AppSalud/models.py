from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre}"

class Doctor(models.Model):
    opciones_especialidad = [
            ('pediatria', 'Pediatría'),
            ('cardiologia', 'Cardiología'),
            ('neurologia', 'Neurología'),
            ('psicologia', 'Psicología'),
            ('traumatologia', 'Traumatología'),
            ('oncologia', 'Oncología'),
            ('otros', 'Otros'),
        ]
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=30, choices = opciones_especialidad)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.especialidad} -- {self.nombre}"


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"{self.fecha} -- {self.paciente}"