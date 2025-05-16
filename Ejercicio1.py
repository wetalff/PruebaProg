#Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de
#la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por
#sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por
#sección, así como el total general de la semana.

Secciones = 3 #Asignando valores a las constantes.
Dias = 5
Estudiantes = 6
Total_semana = 0
print("-"*100) #Añadiendo un separador para que se lea mas facil.
print("A continuacion te pedire las asistencias de los 6 estudiantes de 3 secciones en los dias de clases de una semana")
for seccion in range(Secciones): #Añado el primer bucle "for" en secciones.
    Asistencias = 0 
    No_asistencias = 0
    for dia in range(Dias): #Segundo bucle "for" en dias.
        print("-"*100)
        print(f"Te preguntare la asistencia de 6 estudiantes de la seccion {seccion+1} en el dia {dia+1}")
        print("-"*100)
        for estudiante in range(Estudiantes): #Tercer y ultimo bucle "for"
            asistencia = int(input(f"Asistio a clases el estudiante {estudiante+1} en el dia {dia+1}? (Si = 1 /No = 2): "))
            if asistencia == 1: #Uso if para que haga las operaciones siguientes solo si el valor de "asistencia" es "1".
                Asistencias += 1 #Si se cumple el if entonces ira sumando uno al contador de "Asistencias" por cada "1" en "asistencia", cualquier otro valor sera tomado como inasistencia.
            elif asistencia == 2:
                No_asistencias += 1
            else:
                print("Ingrese un valor valido")      #Si se ingresa cualquier otro valor que no sea los indicados lo marcara como error.      
    Total_semana += Asistencias #Suma todas las asistencias en total
    print("-"*100)
    print(f"El total de asistencias por la seccion {seccion+1} es de {Asistencias} Asistencias") #Como esta en el bucle de "seccion" contabilizara las asistencias por sección y las proporcionara"
    print("-"*100)
                
           
print(f"La asistencias totales de los 6 estudiantes de cada una de las 3 secciones en una semana es de {Total_semana} asistencias") #Se ubica afuera del bucle para sumar todas las asistencias en general y asi poder tener las asistencias totales en la semana.
print("-"*100)
            
                 


        