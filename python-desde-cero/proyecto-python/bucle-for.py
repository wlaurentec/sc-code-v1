tecnologias = ["Python", "Java", "C++", "C#", "JavaScript", "PHP", "Ruby", "Go", "Swift", "Kotlin"] 

for tecnologia in tecnologias:
    if tecnologia == "PHP":
        break
    print(tecnologia)

texto = "Esto es un texto"

for letra in texto:
    print(letra)

for i in range(1000):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(5, 10, 2):
    print(i)


letras = ["a", "b", "c", "d", "e"]
numeros = [1, 2, 3] 

for letra in letras:
    for numero in numeros:
        print(letra, numero)
