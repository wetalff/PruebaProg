#Ejercicio 1: Registro de asistencia académica
#Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de
#la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por
#sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por
#sección, así como el total general de la semana.


# Guardamos total general
total_general = 0

# Recorremos 3 secciones
for seccion in range(1, 4):
    print(f"\nRegistrando asistencia para la sección {seccion}")
    total_seccion = 0
    
    # Recorremos 5 días
    for dia in range(1, 6):
        print(f"  Día {dia}")
        
        # Recorremos 6 estudiantes por día
        for estudiante in range(1, 7):
            while True:  # Bucle para validar la respuesta
                asistencia = input(f"¿Estudiante {estudiante} asistió? (s/n): ").lower()
                
                if asistencia == 's':
                    total_seccion += 1
                    total_general += 1
                    break  # Salimos del bucle si la respuesta es válida
                elif asistencia == 'n':
                    break  # No sumamos nada, pero es válido
                else:
                    print("Respuesta no válida. Por favor escribe 's' o 'n'.")
    
    print(f"Total de asistencias en la sección {seccion}: {total_seccion}")

print(f"\nTotal general de asistencias en la semana: {total_general}")



 