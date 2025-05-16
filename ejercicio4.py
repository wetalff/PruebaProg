"""Ejercicio 4: Monitoreo del consumo energético
Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
generar el promedio semanal correspondiente."""

for edificio in range(1, 5):  # 4 edificios
    print(f"\nEdificio {edificio}")
    total_consumo = 0  

    for dia in range(1, 8):  # 7 días
        print(f"  Día {dia}")
        for turno in ["mañana", "tarde", "noche"]:  # 3 turnos por día
            while True:
                try:
                    consumo = float(input(f"    Consumo en {turno}: "))
                    if consumo < 0:
                        print("El consumo no puede ser negativo. Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")
            total_consumo += consumo  

    promedio = total_consumo / 7  # Promedio diario

    print(f"\nTotal semanal del Edificio {edificio}: {total_consumo:.2f} kw")
    print(f"Promedio diario: {promedio:.2f} kw")
