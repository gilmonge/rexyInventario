Documentacion de tags 
    https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#built-in-tag-reference

Para dar color a los tags de djando en VSCode
    Django Template

En cada Entorno ejecutar 
    conda install pylint

Lint para django
    pip install pylint-django

    Se debe ir a configuracion y buscar pylintArgs y en el ultimo agregar lo siguiente
        --errors-only
        --load-plugins
        pylint_django

Saber version de DJango 
    python -m django --version

Comandos DJango
    crear proyecto
        django-admin startproject webempresa 

    Crear Migracion a db 
        python manage.py makemigrations portfolio
        python manage.py migrate portfolio

    Migrar db 
        python manage.py migrate

    Crear App
        python manage.py startapp core


    Para que Django pueda manejar imagenes
        pip install Pillow

    Crear el super administrador
        python manage.py createsuperuser

    Instalar el editor de texto
        pip install django-ckeditor

    Deployar
        pip install -r requirements.txt

        python manage.py check --deploy

        python manage.py collectstatic