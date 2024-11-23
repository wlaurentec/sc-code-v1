# Estos son los tipos de variables

# String
variableString = "Esto es un string"
print(variableString)

# Integer
variableInteger = 10
print(variableInteger)

# Float
variableFloat = 10.5
print(variableFloat)

# Complex
variableComplex = 1j
print(variableComplex)

# Boolean
variableBoolean = True
print(variableBoolean)

# List
variableList = ["Esto es un string", 10, 10.5, True]
print(variableList)

# Tuple o Tupla de datos inmutables
variableTuple = ("Esto es un string", 10, 10.5, True)
print(variableTuple)

# Dictionary
variableDictionary = {
    "clave1": "Esto es un string",
    "clave2": 10,
    "clave3": 10.5,
    "clave4": True
}
print(variableDictionary)

# Set o Conjunto de datos únicos sin orden o índice real o posición mutable
variableSet = {"Esto es un string", 10, 10.5, True}
print(variableSet)

# frozenset o Conjunto de datos únicos sin orden o índice real o posición inmutable
variableFrozenSet = frozenset({"Esto es un string", 10, 10.5, True})
print(variableFrozenSet)

# range
range = range(10)
print(range)

# None
variableNone = None
print(variableNone)

# Función
def miFuncion():
    print("Esto es una función")

# Clase
class MiClase:
    pass

# Objeto
miObjeto = MiClase()

# Módulo
# import miModulo

# Archivo
# miArchivo = open("archivo.txt", "r")

# Excepción
try:
    1 / 0
except Exception as e:
    print(e)