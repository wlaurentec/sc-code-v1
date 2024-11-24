frutas = [ "manzana", "pera", "banana", "naranja", "mango" ]
print(frutas)

longitud = len(frutas)
print(longitud)

listaStrings = [ "manzana", "pera", "banana", "naranja", "mango" ]
print(listaStrings)

listaNumeros = [ 1, 2, 3, 4, 5 ]
print(listaNumeros)

listaMixta = [ "manzana", 2, "banana", 4, "naranja", 6, "mango" ]
print(listaMixta)

tipo = type(frutas)
print(tipo)

listaDesdeConstructor = list(("manzana", "pera", "banana", "naranja", "mango"))
print(listaDesdeConstructor)

# Verificar si un elemento está en la lista

frutas = [ "manzana", "pera", "banana", "naranja", "mango" ]
print("manzana" in frutas)

if "manzana" in frutas:
    print("La manzana está en la lista")
else:
    print("La manzana no está en la lista")

# Cambiar un elemento de la lista

tecnologias = ["Python", "Java", "C++", "C#", "JavaScript", "PHP", "Ruby", "Go", "Swift", "Kotlin"]
print(tecnologias)

tecnologias[0] = "PHP"

print(tecnologias)

tecnologias[0:3] = ["PHP", "Ruby", "Go"]

print(tecnologias)

# Agregar un elemento a la lista

tecnologias.append("HTML")
print(tecnologias)

tecnologias.insert(1, "CSS")
print(tecnologias)

fronted = ["HTML", "CSS", "JavaScript"]
tecnologias.extend(fronted)
print(tecnologias)

# Eliminar un elemento de la lista

tecnologias.remove("CSS")
print(tecnologias)

tecnologias.pop() # Elimina el último elemento de la lista
print(tecnologias)

tecnologias.pop(0) # Elimina el elemento de la posición 0 de la lista
print(tecnologias)

del tecnologias[0] # Elimina el elemento de la posición 0 de la lista
print(tecnologias)

listaABorrar = ["HTML", "CSS", "JavaScript"]

listaABorrar.clear() # Elimina todos los elementos de la lista
print(listaABorrar)

# Recorrer una lista

print("""for tecnologia in tecnologias:
    print(tecnologia)""")

for tecnologia in tecnologias:
    print(tecnologia)

print("""for i in range(len(tecnologias)):
    print(tecnologias[i])""")

for i in range(len(tecnologias)):
    print(tecnologias[i])

[print(tecnologia) for tecnologia in tecnologias]

for i in range(len(tecnologias)):
    print(f"{i+1}: {tecnologias[i]}")

[print(f"{i+1}: {tecnologias[i]}") for i in range(len(tecnologias))]

# Ejemplo práctico

listaConI = []

print(tecnologias)

for tecnologia in tecnologias:
    if "i" in tecnologia:
        listaConI.append(tecnologia)

print(listaConI)

lista2conO = [tecnologia for tecnologia in tecnologias if "o" in tecnologia]

print(lista2conO)

# Ordenar una lista

tecnologias.sort()
print(tecnologias)

tecnologias.sort(reverse=True)
print(tecnologias)

tecnologias.sort(key=len)
print(tecnologias)

tecnologias.sort(key=len, reverse=True)
print(tecnologias)

tecnologias.reverse()
print(tecnologias)

# Copiar una lista

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
meses2 = meses.copy()
print(meses2)

meses2 = list(meses)
print(meses2)

meses2 = meses[:]
print(meses2)

meses2 = meses
print(meses2)