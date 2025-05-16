""" Ejercicio 2: Uso de computadoras en laboratorios
Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del
campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora
se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con
valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras
ocupadas y libres por laboratorio."""

ocupadas_lab1 = 0
libres_lab1 = 0
ocupadas_lab2 = 0
libres_lab2 = 0

print("Laboratorio 1")
for fila in range(1, 6):  # 5 filas
    for compu in range(1, 5):  # 4 computadoras por fila
        while True:
            try:
                estado = int(input(f"Fila {fila}, Computadora {compu} (1=Ocupada, 0=Libre): "))
                if estado == 1:
                    ocupadas_lab1 += 1
                    break
                elif estado == 0:
                    libres_lab1 += 1
                    break
                else:
                    print("Entrada inválida. Por favor, ingrese 1 (ocupada) o 0 (libre).")

print("\nLaboratorio 2")
for fila in range(1, 6):
    for compu in range(1, 5):
        while True:
            try:
                estado = int(input(f"Fila {fila}, Computadora {compu} (1=Ocupada, 0=Libre): "))
                if estado == 1:
                    ocupadas_lab2 += 1
                    break
                elif estado == 0:
                    libres_lab2 += 1
                    break
                else:
                    print("Entrada inválida. Por favor, ingrese 1 (ocupada) o 0 (libre).")

print("\nResumen de uso de computadoras:")
print(f"Laboratorio 1 - Ocupadas: {ocupadas_lab1}, Libres: {libres_lab1}")
print(f"Laboratorio 2 - Ocupadas: {ocupadas_lab2}, Libres: {libres_lab2}")
