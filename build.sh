#!/usr/bin/env bash
#exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate


correo_electronico="clv@gmail.com"
contrasena="contrasegura"

# Crear un superusuario
echo "from django.contrib.auth.models import User; User.objects.create_superuser('${correo_electronico}', '${contrasena}')" | python manage.py shell

echo "Superusuario creado con éxito."

#Puedes agregar más comandos según sea necesario
#Otros comandos que puedas necesitar ejecutar después de la creación del superusuario

#Finalizar con un mensaje
echo "¡Script de construcción completado con éxito!"