# PreEntrega3 - Flavia Ochoa
Proyecto creado para la Pre Entrega 3 de Coder House por Flavia Ochoa Martinez.

## Introducción
Esta es una web para una clínica, donde se pueden crear Pacientes, Doctores y agendar una cita.

## Orden
1. Primero hacer las migraciones de ser necesario: `python manage.py makemigrations`
2. Seguido del migrate: `python manage.py migrate`
3. Finalmente para correr el servidor: `python manage.py runserver`

## Modelos
Esta página tiene 3 modelos creados
+ Paciente: Nombre, fecha de nacimiento, dirección y teléfono
+ Doctor: Nombre, Especialidad, Teléfono, correo
+ Cita: Paciente, Médico, Fecha, Motivo

## Formularios
### Para insertar datos
+ Crear Paciente
+ Crear Doctor
+ Agendar cita
### Para buscar datos
+ Buscar cita
  
## URLS
Los urls funcionales de mi proyecto son:
+  Home: `http://localhost:8000/`
+  Portal Doctores: `http://localhost:8000/crear_doctor/`
+  Crear Usuario: `http://localhost:8000/crear_usuario/`
+  Agendar cita: `http://localhost:8000/agendar_cita/`
+  Búsqueda de cita: `http://localhost:8000/buscar_cita/`
