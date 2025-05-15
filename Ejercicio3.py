#Ejercicio 3: Control de ventas en feria universitaria
#Facultad de Ingeniería y Arquitectura | Ingeniería en Sistemas de Información
#Cree un programa que permita llevar un registro de ventas en una feria estudiantil organizada
#por la UAM. La feria se desarrollará durante tres días, con cuatro stands por día. Cada stand
#ofrecerá tres productos distintos. El sistema deberá permitir ingresar el monto de venta por
#producto y mostrar un resumen por stand, por día, y un total general de la feria.

total_general = 0  # Acumulador para todas las ventas

# 3 días de feria
for dia in range(1, 4):
    print(f"\n Día {dia} de la feria")
    total_dia = 0  # Acumulador por día

    # 4 stands por día
    for stand in range(1, 5):
        print(f"Stand {stand}")
        total_stand = 0  # Acumulador por stand

        # 3 productos por stand
        for producto in range(1, 4):
            while True:
                try:
                    venta = float(input(f"Monto vendido del producto {producto}: "))
                    if venta < 0:
                        print("No puedes ingresar una venta negativa.")
                    else:
                        break
                except ValueError:
                    print("Por favor, escribe un número válido.")

            total_stand += venta

        # Mostrar total del stand
        print(f"Total del stand {stand}: {total_stand:.2f} C$")

        total_dia += total_stand  # Sumar al total del día

    # Mostrar total del día
    print(f"\n Total del día {dia}: {total_dia:.2f} C$")

    total_general += total_dia  # Sumar al total general

# Mostrar total de toda la feria
print(f"\n Total de la feria: {total_general:.2f} C$")
