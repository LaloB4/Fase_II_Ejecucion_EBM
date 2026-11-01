
# Imagen base
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación y modelo
COPY app.py .
COPY modelo_entrenado.pkl .
COPY frontend/ ./frontend/

# Exponer puerto
EXPOSE 8000

# Ejecutar API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]