# Funciones lambdas son funciones anonimas que se crean con una sola linea
# Se pueden usar para crear funciones pequenias y rapidas


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

""" suma_lambda = lambda a, b: a + b
resta_lambda = lambda a, b: a - b
multiplicar_lambda = lambda a, b: a * b
dividir_lambda = lambda a, b: a / b """


def creador_funciones_multiplicar(n):
    return lambda a: a * n

print(creador_funciones_multiplicar(5)(10))

duplicar = creador_funciones_multiplicar(2)
triplicar = creador_funciones_multiplicar(3)
cuadruplicar = creador_funciones_multiplicar(4)

print(duplicar(10))
print(triplicar(10))
print(cuadruplicar(10))

# Ejemplo lambda filter

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
impares = list(filter(lambda x: x % 2 != 0, numeros))

print(pares)
print(impares)