#Ejercicio 2: Uso de computadoras en laboratorios
#Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del
#campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora
#se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con
#valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras
#ocupadas y libres por laboratorio

# Creamos un ciclo para cada laboratorio
for lab in range(1, 3):
    print(f"\n Laboratorio {lab}")
    
    # Contadores de estado
    ocupadas = 0
    libres = 0

    # 5 filas
    for fila in range(1, 6):
        print(f" Fila {fila}")

        # 4 computadoras por fila
        for pc in range(1, 5):
            while True:  # Validamos la respuesta
                estado = input(f"¿Computadora {pc} está ocupada (o) o libre (l)? ").lower()
                
                if estado == 'o':
                    ocupadas += 1
                    break
                elif estado == 'l':
                    libres += 1
                    break
                else:
                    print("Respuesta inválida. Escribe 'o' para ocupada o 'l' para libre.")

    # Resultados del laboratorio actual
    print(f"\n Laboratorio {lab} - Resultado:")
    print(f"Computadoras ocupadas: {ocupadas}")
    print(f"Computadoras libres: {libres}")
