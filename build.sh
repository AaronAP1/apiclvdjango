#!/usr/bin/env bash
exit on error
set -o errexit

#pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate



nombre_de_usuario="clvsuper"
correo_electronico="xdxd@ejemplo.com"
contrasena="contrasegura"

Verificar si el superusuario ya existe
if python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='${nombre_de_usuario}', is_superuser=True).exists())" | grep "True" &> /dev/null; then
    echo "El superusuario ya existe. No se creará uno nuevo."
else
    # Crear un superusuario
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('${nombre_de_usuario}', '${correo_electronico}', '${contrasena}')" | python manage.py shell
    echo "Superusuario creado con éxito."
fi

Puedes agregar más comandos según sea necesario
Otros comandos que puedas necesitar ejecutar después de la creación del superusuario
...
Finalizar con un mensaje
echo "¡Script de construcción completado con éxito!"