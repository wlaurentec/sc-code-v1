from traceback import print_tb


diccionario = {
    "nombre": "Miguel",
    "tecnologias": ["Python", "Java", "C++"],
    "edad": 30,
    "ciudad": "Madrid",
    "direccion": {
        "calle": "Calle 1",
        "numero": 1
    }
}

print(diccionario)

tipo = type(diccionario)
print(tipo)

longitud = len(diccionario)
print(longitud)

print(diccionario["nombre"])
print(diccionario["tecnologias"])
print(diccionario["edad"])
print(diccionario["ciudad"])
print(diccionario["direccion"]["calle"])
print(diccionario["direccion"]["numero"])

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

if "tecnologias" in diccionario:
    print("El diccionario contiene la clave 'tecnologias'")
else:
    print("El diccionario no contiene la clave 'tecnologias'")

# Cambiar el valor de una clave

diccionario["tecnologias"] = ["Python", "Java", "C++", "C#", "JavaScript", "PHP", "Ruby", "Go", "Swift", "Kotlin"]

print(diccionario["tecnologias"])

diccionario.update({"direccion": {"calle": "Calle 2", "numero": 2}})

print(diccionario)

# Agregar una nueva clave al diccionario

diccionario["telefono"] = "123456789"
diccionario.update({"profesion": "Desarrollador"})

print(diccionario)

# Eliminar una clave del diccionario

del diccionario["telefono"]
del diccionario["profesion"]

diccionario.pop("direccion") # Elimina la clave "direccion"
diccionario.popitem() # Elimina el último elemento

del diccionario["edad"]

# diccionario.clear() # Elimina todos los elementos

print(diccionario)

# Bucles para diccionarios

curso_python = {
    "nombre": "Curso de Python",
    "profesor": "Miguel",
    "estudiantes": 50,
    "dificultad": "Fácil"
}

for key in curso_python:
    print(key)

for value in curso_python.values():
    print(value)

for clave, valor in curso_python.items():
    print(f"{clave}: {valor}")

# Copiar un diccionario

otro_curso_python = curso_python.copy()
otro_curso_python_2 = dict(curso_python)

print(otro_curso_python)
print(otro_curso_python_2)


# Diccionarios anidados

empleados = {
    "empleados": [
        {
            "nombre": "Miguel",
            "edad": 30,
            "ciudad": "Madrid"
        },
        {
            "nombre": "Pedro",
            "edad": 25,
            "ciudad": "Barcelona"
        }
    ]
}

print(empleados)

hijo1 = {
    "nombre": "Miguel",
    "edad": 30,
    "ciudad": "Madrid"
}

hijo2 = {
    "nombre": "Pedro",
    "edad": 25,
    "ciudad": "Barcelona"
}

padre = {
    "hijos": [hijo1, hijo2]
}

print(padre)

familia = {
    "padre": padre,
    "hijos": [hijo1, hijo2]
}

print(familia)

otra_familia = {
    "hijo1": hijo1,
    "hijo2": hijo2
}

print(otra_familia)

for x, obj in otra_familia.items():
    print(x)
    for y in obj:
        print(y, obj[y])