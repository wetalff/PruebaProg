#Ejercicio 4: Monitoreo del consumo energético
#Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
#universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
#tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
#generar el promedio semanal correspondiente.

# Creamos una lista con los nombres de los edificios
edificios = ["Aulas", "Biblioteca", "Laboratorios", "Cafetería"]

# Vamos a recorrer los edificios uno por uno
for edificio in edificios:
    print(f"\n Registro para el edificio: {edificio}")
    
    total_consumo = 0  # Aquí vamos a sumar el consumo total de la semana

    # Por cada día de la semana (7 días)
    for dia in range(1, 8):
        print(f"\n Día {dia}")
        
        # Recorremos los turnos del día
        for turno in ["mañana", "tarde", "noche"]:
            while True:
                try:
                    consumo = float(input(f"Ingrese el consumo en kW para el turno {turno}: "))
                    if consumo < 0:
                        print("El consumo no puede ser negativo.")
                        continue
                    total_consumo += consumo  # Vamos sumando cada consumo
                    break
                except
                    print(" Entrada no válida. Por favor ingrese un número.")

    # Después de 7 días, mostramos el total y promedio
    promedio = total_consumo / 7
    print(f"\n Total de consumo en {edificio}: {total_consumo:.2f} kW")
    print(f" Promedio semanal en {edificio}: {promedio:.2f} kW")
