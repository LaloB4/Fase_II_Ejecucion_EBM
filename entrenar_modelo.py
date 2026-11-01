
import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Cargar dataset
datos = pd.read_csv("dataset.csv")

# Separar variables
X = datos.drop("falla", axis=1)
y = datos["falla"]

# Dividir datos: 80% entrenamiento, 20% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Entrenar modelo
modelo = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

modelo.fit(X_train, y_train)

# Evaluar modelo
predicciones = modelo.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predicciones))
print("\nReporte de clasificación:")
print(classification_report(y_test, predicciones))

# Guardar modelo con pickle
with open("modelo_entrenado.pkl", "wb") as archivo:
    pickle.dump(modelo, archivo)

print("\nModelo guardado correctamente.")
