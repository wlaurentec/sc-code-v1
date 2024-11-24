""" edad = 70

if edad >= 18 and edad <= 65:
    print("Puedes ingresar al bar")
else:
    if edad < 18:
        print("No puedes ingresar al bar porque eres menor de edad")
    else:
        print("No puedes ingresar al bar porque eres jubilado") """


### SHORTHAND

a = 5
b = 10

if a > b: print(f"{a} es mayor que {b}")

print(f"{a} es mayor que {b}") if a > b else print(f"{b} es mayor que {a}")