#Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
#universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
#tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
#generar el promedio semanal correspondiente.

Edificios = 4
Dias = 7
turnos = 3
Total_edificios = 0
print("-"*100)
print("Hola, en este programa calculare el consumo energetico total de 4 edificios en una semana. 👌")
print("-"*100)
for edificio in range(Edificios):
    kilov_edificios = 0
    print(f"A continuacion ingresara el consumo de kilovatios de la semana del edificio {edificio + 1}")
    print("-"*100)
    for dia in range(Dias):
        print("-"*100)
        print(f"Ahora ingresara el consumo de kilovatios en el dia {dia + 1}")
        print("-"*100)
        for turno in range(turnos):
            kilovatios = float(input(f"Ingrese el consumo de kilovatios en el turno {turno + 1}: "))
            kilov_edificios += kilovatios
            Total_edificios += kilovatios 
            prom_sem = Total_edificios / Edificios
    print("-"*100)
    print(f"El consumo total de kilovatios de el edificio {edificio + 1} es de {kilov_edificios} kW")
    print("-"*100)
print(f"El promedio de consumo de kilovatios de los 4 edificios por semana es de {prom_sem} kW")
print("-"*100)    
    