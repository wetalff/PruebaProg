#Cree un programa que permita llevar un registro de ventas en una feria estudiantil organizada
#por la UAM. La feria se desarrollará durante tres días, con cuatro stands por día. Cada stand
#ofrecerá tres productos distintos. El sistema deberá permitir ingresar el monto de venta por
#producto y mostrar un resumen por stand, por día, y un total general de la feria.

feria = 1
stands = 4
dias = 3
productos = 3
Total_feria = 0

total_stand1 = 0
total_stand2 = 0
total_stand3 = 0
total_stand4 = 0
print("-"*100)
print("A continuacion te preguntare el monto de venta de los productos realizadas por los stands durante los 3 dias que dura la feria")
  
for dia in range(dias):     
   Total_dia = 0
   print("-"*100)
   print(f"Ahora indicara el monto de venta de los stands en el dia {dia + 1}")
   for stand in range(stands):
     Total_stand = 0
     print("-"*100)
     print(f"Ingrese el monto de venta de los productos del stand {stand + 1}")
     print("-"*100)
     for producto in range(productos):
         monto_venta_prod = float(input(f"Ingrese el monto de venta del producto {producto + 1}: "))
        
         Total_dia += monto_venta_prod
         Total_feria += monto_venta_prod
         Total_stand += monto_venta_prod
     if stand == 0:
       total_stand1 += Total_stand
     elif stand == 1:
       total_stand2 += Total_stand
     elif stand == 2:
       total_stand3 += Total_stand
     elif stand == 3:
       total_stand4 += Total_stand


   print("-"*100)  
   print(f"Total del día {dia + 1}: {Total_dia} córdobas.")
   print("-"*100)
     
print("Total de ventas por stand durante los 3 días:")
print(f"  Stand 1: {total_stand1} córdobas.")
print(f"  Stand 2: {total_stand2} córdobas.")
print(f"  Stand 3: {total_stand3} córdobas.")
print(f"  Stand 4: {total_stand4} córdobas.")
print("-"*100)
print(f"Las ventas totales de los 4 stands durante los 3 dias de feria son de {Total_feria} Cordobas.")       
print("-"*100)        
                
        
             
                   

