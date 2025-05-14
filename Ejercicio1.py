#Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de
#la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por
#sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por
#sección, así como el total general de la semana.

Secciones = 3
Dias = 5
Estudiantes = 6
Total_semana = 0
print("A continuacion te pedire las asistencias de los 6 estudiantes de 3 secciones en los dias de clases de una semana")
for seccion in range(Secciones): 
    Asistencias = 0
    for dia in range(Dias):
        print(f"te preguntare la asistencia de 6 estudiantes de la seccion {seccion+1} en el dia {dia+1}")
        for estudiante in range(Estudiantes):
            asistencia = int(input(f"Asistio a clases el estudiante {estudiante+1} en el dia {dia+1}? (Si = 1 /No = 2): "))
            if asistencia == 1:
                Asistencias += 1
    Total_semana += Asistencias
    print(f"El total de asistencias por la seccion {seccion+1} es de {Asistencias} Asistencias")
                
           
print(f"La asistencias totales de los 6 estudiantes de cada una de las 3 secciones en una semana es de {Total_semana} asistencias")
            
                
            



        