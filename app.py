
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from pathlib import Path
import pandas as pd
import pickle

app = FastAPI()

# Cargar modelo entrenado
with open("modelo_entrenado.pkl", "rb") as archivo:
    modelo = pickle.load(archivo)

# Definir datos de entrada
class Maquina(BaseModel):
    temperatura: float
    vibracion: float
    horas_operacion: int
    presion: float

# Endpoint de predicción
@app.post("/predict")
def predecir(maquina: Maquina):

    datos = pd.DataFrame([maquina.model_dump()])

    prediccion = int(modelo.predict(datos)[0])

    return {
        "falla": prediccion,
        "resultado": "Riesgo de falla" if prediccion == 1 else "Sin falla"
    }

# Endpoint de para fórmulario de predicción
@app.get("/")
def inicio():
    return FileResponse(
        Path(__file__).resolve().parent / "frontend" / "index.html"
    )