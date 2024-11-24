x = 1

""" while x < 10:
    if x == 5:
        break
    print(x)
    x += 1 """

while x <= 10:
    print(f"Hola a todos esto es un bucle while y x es igual a {x} " )
    x += 1
else:
    print(f"Ya no se cumple la condición del bucle while x es igual a {x}")

while True:
    print("No te olvides de suscribirte a mi canal de youtube")
    respuesta = input("Deseas continuar? S/N: ").strip().lower()
    if respuesta == "s":
        break