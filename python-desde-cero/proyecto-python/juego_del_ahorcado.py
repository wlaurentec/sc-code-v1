import random

def obtener_palabra_secreta() -> str:
    palabras = [
        "python",
        "java",
        "kotlin",
        "javascript",
        "php",
        "c",
        "c++",
        "ruby",
        "swift",
        "go",
    ]
    return random.choice(palabras)


def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinido = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinido += letra
        else:
            adivinido += "_"
    return adivinido


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta.")
    print(
        mostrar_progreso(palabra_secreta, letras_adivinadas),
        "La cantidad de letras es:",
        len(palabra_secreta),
    )

    while not juego_terminado and intentos > 0:
        adivinanza = input("Ingresa una letra: ").lower()

        if len(adivinanza) != 1 and adivinanza.isalpha():
            print("Ingresa una letra válida (una sola letra).")
        elif adivinanza in letras_adivinadas:
            print(f"Ya has adivinado la letra {adivinanza}. Prueba con otra letra.")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"Muy bien! Has adivinado la letra '{adivinanza}'.")
            else:
                intentos -= 1
                print(f"La letra {adivinanza} no está en la palabra secreta.")
                print(f"Tienes {intentos} intentos restantes.")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            palabra_secreta = palabra_secreta.capitalize()
            juego_terminado = True
            print(
                f"¡Felicidades! Has adivinado la palabra secreta es: '{palabra_secreta}'."
            )

    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()

        juego_terminado = True
        print(f"¡Has perdido! La palabra secreta era {palabra_secreta}.")

    print("¡Gracias por jugar!")


juego_ahorcado()
