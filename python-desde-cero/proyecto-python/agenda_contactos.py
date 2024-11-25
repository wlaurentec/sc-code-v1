def mostrar_menu():
    print("\nAgenda de Contactos")
    print("1. Agregar nuevo contacto")
    print("2. Elminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")


def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    correo = input("Ingrese el correo electrónico del contacto: ")
    agenda[nombre] = {"Teléfono": telefono, "Correo": correo}
    print(f"Contacto {nombre} agregado correctamente.")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado correctamente.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea buscar: ")
    if nombre in agenda:
        print(f"Contacto {nombre}:")
        print(f"Teléfono: {agenda[nombre]['Teléfono']}")
        print(f"Correo electrónico: {agenda[nombre]['Correo']}")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos:")
        for nombre, datos in agenda.items():
            print(f"Contacto: {nombre}")
            print(f"Teléfono: {datos['Teléfono']}")
            print(f"Correo electrónico: {datos['Correo']}")
            print()
    else:
        print("La agenda de contactos está vacía.")

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

    print("Gracias por usar la agenda de contactos.")

agenda_contactos()