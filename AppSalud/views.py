from django.shortcuts import render
from django.http import HttpResponse
from AppSalud.models import Paciente, Doctor, Cita
from AppSalud.forms import PacienteFormulario, DoctorForm, CitaForm

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def crear_paciente(request):
        if request.method == "POST":
            formulario = PacienteFormulario(request.POST) #almacena la informacion el form

            if formulario.is_valid():
                infopac = formulario.cleaned_data #convierte la info del form a un diccionario de python

                paciente_nuevo = Paciente(
                    nombre = infopac["nombre"],
                    fecha_nacimiento = infopac["fecha_nacimiento"],
                    direccion = infopac["direccion"],
                    telefono = infopac["telefono"],
                    )
                
                paciente_nuevo.save()
                return render(request, "inicio.html")
            
        else:
            formulario = PacienteFormulario()

        return render(request, "crear_paciente.html", {"formu":formulario})


def crear_doctor(request):
        if request.method == "POST":
            formulario = DoctorForm(request.POST) #almacena la informacion el form

            if formulario.is_valid():
                infodoc = formulario.cleaned_data #convierte la info del form a un diccionario de python

                doctor_nuevo = Doctor(
                    nombre = infodoc["nombre"],
                    especialidad = infodoc["especialidad"],
                    telefono = infodoc["telefono"],
                    correo = infodoc["correo"],
                    )
                
                doctor_nuevo.save()
                return render(request, "inicio.html")
            
        else:
            formulario = DoctorForm()

        return render(request, "crear_doctor.html", {"formu":formulario})

def agendar_cita(request):
    infocita = {}

    if request.method == 'POST':
        formulario = CitaForm(request.POST)
        
        if formulario.is_valid():
             infocita = formulario.cleaned_data #convierte la info del form a un diccionario de python

        cita_nueva = Cita.objects.create(
                paciente= infocita.get("paciente"),
                medico= infocita.get("medico"),
                fecha= infocita.get("fecha"),
                motivo= infocita.get("motivo"),     
        )

        cita_nueva.save()
        return render(request, "inicio.html")
    
    else:
        form = CitaForm()

    return render(request, 'agendar_cita.html', {'formu': form})



def buscar_cita(request):
    
    if request.GET:
        paciente = request.GET["paciente"]  #leer el diccionario de info del formulario y obtengo el valor de busqueda
        cita = Cita.objects.filter(paciente__nombre__icontains=paciente) #filtrar todos los cursos que tengan dicho nombre!!
        #motivo = motivo.objects.filter(paciente__contains=paciente)

        mensaje = f"Estamos buscando las citas del paciente {paciente}"

        return render(request, "buscar_cita.html", {"mensaje":mensaje, "resultados":cita})

    
    return render(request, "buscar_cita.html") #si todavia no hay una busqueda