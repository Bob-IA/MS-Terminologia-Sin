# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto en el que Flask está ejecutándose
EXPOSE 8081

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
