variableGlobal = "Esto es una variable global"

def miFuncion():
    variableGlobal = "Esto es una variable global desde la función"
    variableLocal = "Esto es una variable local"
    print(variableGlobal)
    print(variableLocal)

miFuncion()

print(variableGlobal)
print(variableLocal)