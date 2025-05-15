#Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del
#campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora
#se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con
#valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras
#ocupadas y libres por laboratorio.

Laboratorios = 2
filas = 5
computadoras = 4
print("-"*165)
print("¡Hola!, soy un programa que automaticamente te contabilizara el numero de computadoras libres y ocupadas por laboratorio, solo me tendras que decir si estan libres o ocupadas. 😁")
print("-"*165)
for lab in range(Laboratorios):
    Estado_libre = 0
    Estado_ocupado = 0
    print(f"Ahorita aclarara si las computadoras del laboratorio {lab + 1} estan libres o ocupadas")
    print("-"*100)
    for fila in range(filas):
        print(f"Mencione que computadoras estan disponibles o ocupadas en esta fila numero {fila + 1}")
        print("-"*100)
        for computadora in range(computadoras):
            Estado = int(input(f"¿Cual es el estado de la computadora numero {computadora + 1}? (Libre = 1 / Ocupada = 2): "))
            if Estado == 1:
                Estado_libre += 1
            if Estado == 2:
                Estado_ocupado += 1
    print("-"*133)
    print(f"El resumen total de computadoras libres en el laboratorio numero {lab + 1} es de {Estado_libre} computadoras y el numero de ocupadas es de {Estado_ocupado} computadoras")

 

    
  