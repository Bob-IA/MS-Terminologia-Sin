# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt y luego instala las dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al directorio de trabajo
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8081

# Definir la variable de entorno que define el host
ENV PYTHONUNBUFFERED True

# Comando para ejecutar la aplicación
CMD ["gunicorn", "-w", "4", "-t", "120", "-b", ":8080", "app.py:app"]
