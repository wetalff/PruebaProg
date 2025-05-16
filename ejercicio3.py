"""Ejercicio 3: Control de ventas en feria universitaria
Facultad de Ingeniería y Arquitectura | Ingeniería en Sistemas de Información
Cree un programa que permita llevar un registro de ventas en una feria estudiantil organizada
por la UAM. La feria se desarrollará durante tres días, con cuatro stands por día. Cada stand
ofrecerá tres productos distintos. El sistema deberá permitir ingresar el monto de venta por
producto y mostrar un resumen por stand, por día, y un total general de la feria.
"""

total_feria = 0  

for dia in range(1, 4):  # 3 días
    print(f"\nDÍA {dia}")
    total_dia = 0  # Ventas por día

    for stand in range(1, 5):  # 4 stands por día
        print(f"\n  STAND {stand}")
        total_stand = 0  # Ventas por stand

        for producto in range(1, 4):  # 3 productos por stand
            venta_valida = False
            while not venta_valida:
                entrada = input(f"    Producto {producto} - Monto de venta: $")
                if entrada.replace('.', '', 1).isdigit():
                    venta = float(entrada)
                    if venta >= 0:
                        total_stand += venta
                        venta_valida = True
                    else:
                        print("El monto no puede ser negativo. Intente de nuevo.")
                else:
                    print("Entrada inválida. Ingrese un número válido.")

        print(f"  Total del Stand {stand}: ${total_stand:.2f}")
        total_dia += total_stand  

    print(f"\nTotal del Día {dia}: ${total_dia:.2f}")
    total_feria += total_dia  

print(f"\nTotal General de la feria: ${total_feria:.2f}")
