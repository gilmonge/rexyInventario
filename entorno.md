# Configuración entorno para Node para cada proyecto
## Activación del ambiente
Si ya se tiene configurado el entorno se debe ejecutar lo siguiente
```ssh
..\envPy\Scripts\activate
source ../envPyUbuntu/bin/activate
```
Se debe ejecutar según la ubicación del proyecto

## Configuración entorno Python
Administrador de entorno virtual (solo si no se tiene instalado)
ssh
pip install virtualenv

Configuración entorno virtual

1. Instalación
    ```ssh
    py -m venv envPy
    ```
 2. Activación
   ```ssh
   ..\envPy\Scripts\activate
   ```
 3. Instalar requisitos
    ```ssh
    pip install -r requisitos.txt
    ```
 4. Desactivación
    ```ssh
    deactivate
    ```
## Git
Se debe quitar de Git para evitar problemas en el .gitignore agregar
```ssh
envPy
```