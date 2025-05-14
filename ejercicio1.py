""" Ejercicio 1: Registro de asistencia académica
Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de
la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por
sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por
sección, así como el total general de la semana. """

# Se crean 3 variables
asist_A = 0  
asist_B = 0  
asist_C = 0  

for dia in range(1, 6): # Significa contar desde el 1 hasta el 5 (el 6 no se incluye). 
    print(f"Día {dia}")

    # Sección A
    print("Asistencia de la Sección A: ")
    for estudiante in range(1, 7):
        asistio = int(input(f"Estudiante {estudiante} (1=Sí, 0=No): "))
        if asistio == 1: # Igual: ==
            asist_A += 1 # Asignar: +=

    # Sección B
    print("Asistencia de la Sección B: ")
    for estudiante in range(1, 7):
        asistio = int(input(f"Estudiante {estudiante} (1=Sí, 0=No): "))
        if asistio == 1:
            asist_B += 1

    # Sección C
    print("Asistencia de la Sección C: ")
    for estudiante in range(1, 7):
        asistio = int(input(f"Estudiante {estudiante} (1=Sí, 0=No): "))
        if asistio == 1:
            asist_C += 1

# Mostrar las asistencias
print("\nResumen de asistencias en la semana:")
print(f"Total asistencias Sección A: {asist_A}")
print(f"Total asistencias Sección B: {asist_B}")
print(f"Total asistencias Sección C: {asist_C}")
print(f"Total general de asistencias: {asist_A + asist_B + asist_C}") # Asistencia general