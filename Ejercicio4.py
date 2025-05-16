#Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
#universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
#tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
#generar el promedio semanal correspondiente.

Edificios = 4   #Asigno los valores a las constantes.
Dias = 7
Turnos = 3
Total_edificios = 0
print("-"*100)   #Añado separadores.
print("Hola, en este programa calculare el consumo energetico total de 4 edificios en una semana. 👌") #Pequeña descripcion.
print("-"*100)
for edificio in range(Edificios): #Primer bucle "for".
    Kilov_edificios = 0 #Constante añadida dentro del bucle para que se reinicie cada vez que se reinicie el bucle.
    print(f"A continuacion ingresara el consumo de kilovatios de la semana del edificio {edificio + 1}")
    print("-"*100)
    for dia in range(Dias): #Segundo bucle "for".
        print("-"*100)
        print(f"Ahora ingresara el consumo de kilovatios en el dia {dia + 1}")
        print("-"*100)
        for turno in range(Turnos): #Tercer bucle "for".
            Kilovatios = float(input(f"Ingrese el consumo de kilovatios en el turno {turno + 1}: ")) #Pido el consumo de Kilovatios.
            Kilov_edificios += Kilovatios  #Hago la suma para cada respuesta.
            Total_edificios += Kilovatios 
            Prom_sem = Total_edificios / Edificios
    print("-"*100)
    print(f"El consumo total de kilovatios de el edificio {edificio + 1} es de {Kilov_edificios} kW") #Imprimo la respuesta dentro del bucle para que en este caso sume los kilovatios por edificio y no los de todos.
    print("-"*100)
print(f"El promedio de consumo de kilovatios de los 4 edificios por semana es de {Prom_sem} kW") #Imprimo el promedio de consumo de kilovatios y esta vez afuera del bucle porque aqui si necesitamos la de todos los edificios.
print("-"*100)    
    