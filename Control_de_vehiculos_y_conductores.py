print("EJERICIO 8")
print("Control de vehiculosy conductores")

conductores=["Laura", "Mateo", "Julián"]
print(conductores)
conductores.append (input("Ingrese un  nombre de conductor: "))
conductores.append (input("Ingrese un  nombre de conductor: "))

vehiculos=["Moto","Carro","Bicicleta"]
print(vehiculos)
vehiculos.append (input("Ingrese un nombre de un vehiculo: "))
vehiculos.append (input("Ingrese un nombre de un vehiculo: "))


if "Julián" in conductores:
    conductores.append("Santiago")
    print(f"Lista de conductores actualizada {conductores}")
else:
    print("No se cumplió la funcion")

if "Carro" in vehiculos:
    vehiculos.append("Camioneta")
    print(f"Lista de vehiculos actualizada {vehiculos}")
else:
    print("No se cumplió la funcion")

if "Mateo" in conductores:
    conductores.remove("Mateo")
    print(f"Lista de conductores actualizada {conductores}")
else:
    print("No se cumplió la funcion")

if len(vehiculos) >3:
    vehiculos.remove("Moto")
    print(f"La lista actualizada {vehiculos}")
else:
    print("No se cumplió la funcion")


if "Laura" in conductores:
                    conductores.remove("Laura")
                    conductores.append("Luisa")
                    print(f"Lista Actualizada{conductores}")
else:
    print("No se cumple la condicion")


habilitados=[conductores[0],conductores[1]]
movilidad=[vehiculos[-1],vehiculos[-2]]

if "Camioneta" in vehiculos:
    vehiculo_extra=("Camioneta","Disponible")
    print(vehiculo_extra)
else:
    print("No se cumplió la funcion")

if "Luisa" in habilitados:
    habilitados.append("Licencia activa")
    print(habilitados)
else:
    print("No se cumplió la condiccion")

if "Licencia activa" in habilitados:
    registro ={
                "Conductor":"Luisa",
                "Vehiculo_asignado":"Carro",
                "Vigente":True
                    }
else:
    print("No se cumplió la condicion")

