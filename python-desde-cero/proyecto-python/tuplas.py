# TUPLA: Colectión de datos inmutables que no se pueden modificar

# indices: 0, 1, 2, 3
vehiculos = ("coche", "moto", "bicicleta", "autobús", "tren", "avión", "barco")
print(vehiculos)

longitud = len(vehiculos)
print(longitud)

tipo = type(vehiculos)
print(tipo)

tuplaConstructor = tuple(("coche", "moto", "bicicleta", "autobús")) # Construye una tupla a partir de una lista
print(tuplaConstructor)

# Modificar una tupla desde una lista

vehiculos = list(vehiculos)
print(vehiculos)
vehiculos[0] = "camioneta"
vehiculos = tuple(vehiculos)
print(vehiculos)

# Desempaquetar una tupla

vehiculos = ("coche", "moto", "bicicleta", "autobús")
coche, moto, bicicleta, autobus = vehiculos
print(coche)
print(moto)
print(bicicleta)
print(autobus)

coche, moto, *vehiculosAgrupados = vehiculos
print(vehiculosAgrupados)

#  Recorrer una tupla

print("""for vehiculo in vehiculos:
    print(vehiculo)""")

for vehiculo in vehiculos:
    print(vehiculo)

print("""for i in range(len(vehiculos)):
    print(vehiculos[i])""")

for i in range(len(vehiculos)):
    print(vehiculos[i])

[print(vehiculo) for vehiculo in vehiculos]

for i in range(len(vehiculos)):
    print(f"{i+1}: {vehiculos[i]}")

[print(f"{i+1}: {vehiculos[i]}") for i in range(len(vehiculos))]

#  Join de tuplas

citricos = ("limón", "naranja", "mandarina")
tropical = ("melón", "papaya", "kiwi")
frutas = citricos + tropical
print(frutas)

dobleCitricos = citricos * 2
print(dobleCitricos)