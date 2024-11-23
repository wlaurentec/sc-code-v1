import random

numero_entero = 10
numero_decimal = 5.75
numero_complejo = 5 + 2j

""" print(numero_entero)
print(numero_decimal)
print(numero_complejo)

print(type(numero_entero))
print(type(numero_decimal))
print(type(numero_complejo)) """

entero_desde_decimal = int(numero_decimal)
decimal_desde_entero = float(numero_entero)
complejo_desde_entero = complex(numero_entero)
complejo_desde_decimal = complex(numero_decimal)

# print(decimal_desde_entero)
# print(entero_desde_decimal)
# print(complejo_desde_decimal)
# print(complejo_desde_entero)

####### RANDOM

aleatorio = random.random()
aleatorio_entero = random.randrange(1, 10)
aleatorio_par = random.randrange(2, 10, 2)
aleatorio_impar = random.randrange(1, 10, 2)

print(aleatorio)
print(aleatorio_entero)
print(aleatorio_par)
print(aleatorio_impar)