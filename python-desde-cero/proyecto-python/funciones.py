def funcion(profesor, curso):
    print(f"El profesor es {profesor} y el curso es {curso}")

funcion("Miguel", "Python")

funcion(curso="Python", profesor="Miguel")

funcion("Victor", "Java")

# Parametros son la lista de variables dentro de los parentesis
# Argumentos son los valores que se le pasan a la función

def funcionPorGenero(profesor, curso, femenino):
    profesion = "el profesor"
    if femenino:
        profesion = "la profesora"
    print(f"El curso es {curso} lo dara {profesion} {profesor}")

funcionPorGenero("Yovana", "Python", True)
funcionPorGenero("Eduardo", "Python", False)
funcionPorGenero("Luis", "Java", False)


# Argumentos arbitrarios

def llamar_alumnos(*alumnos):
    for alumno in alumnos:
        print(alumno)

llamar_alumnos("Miguel", "Eduardo", "Luis", "Yovana")

def alumnos_destacados(*alumnos):
    print(f"Mi mejor alumno es {alumnos[0]}")
    print(f"Mi alumno mas divertido es {alumnos[1]}")
    print(f"Mi alumno mas inteligente es {alumnos[2]}")

alumnos_destacados("Miguel", "Eduardo", "Luis")

# Argumento clave / key argument

def cursos(curso1, curso2, curso3):
    print(f"El primer curso que dare es {curso1}")
    print(f"El segundo curso que dare es {curso2}")
    print(f"El tercer curso que dare es {curso3}")

cursos("Java", "CSS", "HTML")
cursos(curso3="Java", curso2="CSS", curso1="HTML")

# Argumentos claves arbitrarios

def llamar_alumno(**alumnos):
    print(f"El apellido del alumno es {alumnos['apellido']} y su nombre es {alumnos['nombre']}")

llamar_alumno(apellido="Gutierrez", nombre="Miguel", edad=30)


# Variables por defecto

def nombre_pais(pais="España"):
    print(f"El pais es {pais}")

nombre_pais("Argentina")
nombre_pais()

# Otros tipos de datos que podríamos usar

lista = ["Java", "Python", "C++"]
number = 10

def usar_tipos_de_datos(lista, number):
    print(lista)
    print(number)

usar_tipos_de_datos(["Java", "Python", "JavaScript"], 20)

# Retornar valores de funciones

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b



print(sumar(10, 20))
print(restar(10, 20))
print(multiplicar(10, 20))
print(dividir(10, 20))

# Recursividad

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
