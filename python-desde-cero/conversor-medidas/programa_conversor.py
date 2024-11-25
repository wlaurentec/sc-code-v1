import pandas as pd

def cm_a_pulgadas(cm):
    pulgadas = cm / 2.54
    return pulgadas

# Leer el archivo Excel
df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una nueva columna "Pulgadas" al DataFrame
df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas)

# Guardar el DataFrame en un nuevo archivo Excel
df.to_excel("muebles_medidas_pulgadas.xlsx", index=False)

print("Conversion realizada con exito")