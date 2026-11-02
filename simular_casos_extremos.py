
import pickle
import pandas as pd

# Cargar modelo entrenado
with open("modelo_entrenado.pkl", "rb") as archivo:
    modelo = pickle.load(archivo)

# Definir casos extremos
casos = pd.DataFrame([
    [40, 0.1, 100, 1],
    [120, 10, 9999, 10],
    [65, 2.5, 3000, 4],
    [90, 7, 8000, 8],
    [91, 5, 5000, 6]
], columns=[
    "temperatura",
    "vibracion",
    "horas_operacion",
    "presion"
])

# Realizar predicciones
predicciones = modelo.predict(casos)

# Mostrar resultados
for i, prediccion in enumerate(predicciones):
    resultado = "Riesgo de falla" if prediccion == 1 else "Sin falla"
    print(f"Caso {i + 1}: {resultado}")
