#RONDA 2
#Ejercicio 14
print("\nCalculadora de porcentaje de ganancia")
costo=float(input("Ingrese el costo de su producto: "))
precio=float(input("Ingrese el precio de su producto: "))

gana1=precio-costo
porcentaje1= gana1/costo
porcentaje2= porcentaje1*100

if porcentaje2 > 30:
    print(f"Su porcentaje de ganancia fue de {porcentaje2:.2f}% obtuvo una alta ganancia")
elif porcentaje2 >=10 and porcentaje2 <=30:
    print(f"Su porcentaje de ganancia fue de {porcentaje2:.2f}% obtuvo una ganancia media")
elif porcentaje2 >0 and porcentaje2 <10:
    print(f"Su porcentaje de ganancia fue de {porcentaje2:.2f}% obtuvo una ganancia muy baja")
else:
    print("Usted ha obtenido una perdida")