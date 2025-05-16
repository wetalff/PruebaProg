#Cree un programa que permita llevar un registro de ventas en una feria estudiantil organizada
#por la UAM. La feria se desarrollará durante tres días, con cuatro stands por día. Cada stand
#ofrecerá tres productos distintos. El sistema deberá permitir ingresar el monto de venta por
#producto y mostrar un resumen por stand, por día, y un total general de la feria.


Stands = 4
Dias = 3
Productos = 3        #Asigno valores a las constantes.
Total_feria = 0

Total_stand1 = 0 
Total_stand2 = 0
Total_stand3 = 0
Total_stand4 = 0
print("-"*100)       #Añado separadores.
print("A continuacion te preguntare el monto de venta de los productos realizadas por los stands durante los 3 dias que dura la feria")
  
for dia in range(Dias):   #Primer bucle "for".  
   Total_dia = 0 #Constante dentro del bucle para que se reinicie cada vez que se reinicie el bucle.
   print("-"*100)
   print(f"Ahora indicara el monto de venta de los stands en el dia {dia + 1}")
   for stand in range(Stands): # Segundo bucle "for".
     Total_stand = 0 #Constante dentro del bucle para que se reinicie cada vez que se reinicie el bucle.
     print("-"*100)
     print(f"Ingrese el monto de venta de los productos del stand {stand + 1}")
     print("-"*100)
     for producto in range(Productos): #Tercer y ultimo bucle "for".
         monto_venta_prod = float(input(f"Ingrese el monto de venta del producto {producto + 1}: ")) #Pido el monto de venta.
        
         Total_dia += monto_venta_prod   #Sumo las variables por el monto de ventas.
         Total_feria += monto_venta_prod
         Total_stand += monto_venta_prod
     if stand == 0:                      #Uso el if y el elif para asignar la suma de la variable "Total_stand" a su respectivo stand.
       Total_stand1 += Total_stand
     elif stand == 1:
       Total_stand2 += Total_stand
     elif stand == 2:
       Total_stand3 += Total_stand
     elif stand == 3:
       Total_stand4 += Total_stand


   print("-"*100)  
   print(f"Total del día {dia + 1}: {Total_dia} córdobas.") #Aqui imprimo el total de monto de venta por dia.
   print("-"*100)
     
print("Total de ventas por stand durante los 3 días:") #Aqui se imprime el total del monto de venta de cada uno de los stands por los 3 dias que dura la feria.
print(f"  Stand 1: {Total_stand1} córdobas.")
print(f"  Stand 2: {Total_stand2} córdobas.")
print(f"  Stand 3: {Total_stand3} córdobas.")
print(f"  Stand 4: {Total_stand4} córdobas.")
print("-"*100)
print(f"Las ventas totales de los 4 stands durante los 3 dias de feria son de {Total_feria} Cordobas.") #Aqui se imprime el total de monto de venta durante toda la feria.    
print("-"*100)        
                
        
             
                   

