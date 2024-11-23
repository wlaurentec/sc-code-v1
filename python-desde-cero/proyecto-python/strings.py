# Strings

text = "I believe people have to follow their dreams. I did."

print(text)

print(text[10])

print(text[-1])

print(text[0:10])

print(text[0:10:2])

print(text[0:10:3])

print(text[::2])

length = len(text)

print("Did".lower() in text.lower())

print("Did".upper() in text.upper())

print("Did".title() in text.title())

print(length)

print(text.upper())

print(text.lower())

print(text.title())

print(text.capitalize())

print(text.count("I")) # cuenta la cantidad de I

print(text.find("p")) # encuentra la posición de la I

print(text.replace("I", "We"))

print(text.split(" ")) # divide el string en una lista

print(text.startswith("a"))

print(text.endswith("s"))

# F-Strings

name = "John"
age = 30

print(f"Mi nombre es {name} y tengo {age:.2f} años.")

print(f"El resultado de 70 *30 es {70 * 30}")