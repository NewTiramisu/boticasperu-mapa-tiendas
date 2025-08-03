import pandas as pd
import json

df = pd.read_excel("Lista de boticas.xlsx")

# Eliminar filas vacías y sin datos clave
df = df.dropna(how="all")
df = df.dropna(subset=["SISCOD"])

# Asegurar que SISCOD sea entero
df["SISCOD"] = df["SISCOD"].astype(int)

# Renombrar columnas
df = df.rename(columns={
    "SISCOD": "codigo",
    "BOTICA": "nombre",
    "DIRECCIÓN": "direccion",
    "DISTRITO": "distrito",
    "PROVINCIA": "provincia",
    "DEPARTAMENTO": "departamento",
    "LATITUD": "lat",
    "LONGITUD": "lng"
})

# Convertir a JSON y guardar
tiendas = df.to_dict(orient="records")

with open("tiendas.json", "w", encoding="utf-8") as f:
    json.dump(tiendas, f, ensure_ascii=False, indent=2)

print("Listo: se generó tiendas.json correctamente.")
