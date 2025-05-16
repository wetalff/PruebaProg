#Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del
#campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora
#se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con
#valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras
#ocupadas y libres por laboratorio.

Laboratorios = 2 #Asignando valores a las constantes.
Filas = 5
Computadoras = 4
print("-"*165) #Añadiendo un separador.
print("¡Hola!, soy un programa que automaticamente te contabilizara el numero de computadoras libres y ocupadas por laboratorio, solo me tendras que decir si estan libres o ocupadas. 😁") #Descripcion del programa.
print("-"*165)
for lab in range(Laboratorios): #Primer bucle "for".
    Estado_libre = 0   #Asignando otros valores esta vez dentro del bucle para que la respuestas no se sumen entre ellas.
    Estado_ocupado = 0
    print(f"Ahorita aclarara si las computadoras del laboratorio {lab + 1} estan libres o ocupadas")
    print("-"*100)
    for fila in range(Filas): #Segundo bucle "for".
        print(f"Mencione que computadoras estan disponibles o ocupadas en esta fila numero {fila + 1}")
        print("-"*100)
        for computadora in range(Computadoras): #Tercer bucle "for".
            Estado = int(input(f"¿Cual es el estado de la computadora numero {computadora + 1}? (Libre = 1 / Ocupada = 2): ")) #Aqui ya pregunto si las computadores estan libres "1", o estan ocupadas "2".
            if Estado == 1: #Uso el if para ir sumando valores solamente si se cumple el if en este caso si "Estado" == 1 sumara en la constante Estado_libre.
                Estado_libre += 1
            elif Estado == 2:  #Exactamente lo mismo que en el anterior solo que ahora con las computadoras ocupadas.
                Estado_ocupado += 1
            else:
                print("Ingrese un valor valido")
    print("-"*133)
    print(f"El resumen total de computadoras libres en el laboratorio numero {lab + 1} es de {Estado_libre} computadoras y el numero de ocupadas es de {Estado_ocupado} computadoras")
    print("-"*133)
    #Escribo ya los resultados haciendo enfasis en que solo estan en un bucle en este caso de "lab" para que me escriba los resultados por laboratorio que es como me pide el ejercicio.

 

    
  