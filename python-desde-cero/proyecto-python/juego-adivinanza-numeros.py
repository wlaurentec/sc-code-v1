import random


def juego_adivinanza():
    # Generar un número aleatorio
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    #  Mensaje de bienvenida
    print("¡Bienvenido al juego de adivinanza de números!")
    print("Tienes que adivinar un número entre 1 y 100.")
    print("Intenta adivinarlo!")

    while not adivinado:
        # Pedir al usuario que ingrese un número
        adivinanza = input("Ingresa un número del 1 al 100: ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Convertir a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print("El número es mayor. Intenta nuevamente.")
            elif adivinanza > numero_secreto:
                print("El número es menor. Intenta nuevamente.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                adivinado = True
        else:
            print("Ingresa un número válido del 1 al 100.")


juego_adivinanza()
