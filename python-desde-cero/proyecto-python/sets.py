# SET: colectión de datos desordenados que no se pueden duplicar los datos

conjunto = {1, 2, 3, 2, 5, 6, 7, 9, 9, 10}

print(conjunto)

conjuntoConstructor = set(("aqui", "estoy", "creando", "un", "conjunto"))
print(conjuntoConstructor)

if "aqui" in conjuntoConstructor:
    print("aqui esta")

    # Agregar elementos a un conjunto

telefonos = {"Samsung", "Nokia", "Xiaomi"}
telefonos.add("Huawei")
print(telefonos)

telefonos2 = {"Samsung", "Nokia", "Xiaomi"}
telefonos2.update(["Huawei", "Motorola"])
telefonos.update(telefonos2)
print(telefonos2)

# Eliminar elementos de un conjunto

telefonos = {"Samsung", "Nokia", "Xiaomi"}
telefonos.remove("Samsung")
print(telefonos)

telefonos = {"Samsung", "Nokia", "Xiaomi"}
telefonos.discard("Samsung")
print(telefonos)

telefonos.clear()
print(telefonos)

# Join de conjuntos

a = { 1,2,3,4,5 }
b = { 1,3,5,7,9 }

# Union

c = a.union(b)
print(c)

d = a | b
print(d)

""" a.update(b) # Modifica a
print(a) """

# Intersección

""" a.intersection_update(b) # Modifica a
print(a) """

e = a.intersection(b)
print(e)

f = a & b
print(f)

g = a.difference(b)
print(g)

h = a.symmetric_difference(b)
i = a ^ b
print(h)
print(i)