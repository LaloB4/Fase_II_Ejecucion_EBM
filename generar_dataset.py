
import numpy as np
import pandas as pd

np.random.seed(42)

datos = pd.DataFrame({
    "temperatura": np.random.uniform(40, 120, 2000),
    "vibracion": np.random.uniform(0.1, 10, 2000),
    "horas_operacion": np.random.randint(100, 10000, 2000),
    "presion": np.random.uniform(1, 10, 2000)
})

datos["falla"] = (
    (datos["temperatura"] > 90) |
    (datos["vibracion"] > 7) |
    ((datos["horas_operacion"] > 8000) &
     (datos["presion"] > 8))
).astype(int)

datos.to_csv("dataset.csv", index=False)

print(datos.head())
print(datos["falla"].value_counts())
