# P-MB

Este repositorio tiene un api de pedidos

----

## Requirements

* Python 3.8+
* PostgreSQL 9.4+
* Virtualenvwrapper
* requirements.txt

### PostgreSQL
Para instalar PostgreSQL consulta https://www.postgresql.org/docs/9.5/static/installation.html

### Virtualenvwrapper

Para instalar virtualenvwrapper consulta https://virtualenvwrapper.readthedocs.io/en/latest/, ejecute

```shell
sudo pip3 install virtualenvwrapper
```

Deberá crear un directorio para virtualenv.
```shell
mkdir ~/.virtualenvs
```
Luego, exporta la variable para el directorio
```shell
export WORKON_HOME=~/.virtualenvs
```
Ahora, modifique ~ / .bashrc para agregar las referencias al entorno virtual. Al final de ~ / .bashrc (o ~ / .bash_profile) escriba
```shell
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh
```
y guardar, luego en su terminal ingrese

```shell
source .bashrc
```
Y ahí lo tienes, virtualenvwrapper ahora está instalado. Ahora, para crear un entorno virtual, ejecute el siguiente comando
```shell
mkvirtualenv virtualenv_name
```
donde * virtualenv_name * es el nombre que desea darle a su entorno virtual. Si desea salir del entorno virtual, simplemente escriba "desactivar". Para ingresar nuevamente en el entorno virtual, escriba
```shell
workon virtualenv_name
```

### requirements.txt
Después de clonar la carpeta del proyecto, en la raíz hay un archivo llamado requirements.txt. Este archivo contiene todos los paquetes necesarios para ejecutar la API. Para instalar esos paquetes, en su terminal ejecute
```shell
pip install -r requirements.txt
```

----

## Configuración

En la raíz del proyecto, ejecute
```shell
python manage.py makemigrations
```
para generar las migraciones que faltan. Si no se crea ninguno, está bien. Ahora, para aplicar esas migraciones, ejecute
```shell
python manage.py migrate
```


----

## Correr servidor

Dentro de su entorno virtual, usando su configuración y en la carpeta raíz, ejecute
```shell
python manage.py runserver
```
Y el servidor estará activo, para ingresar a la interfaz de Django REST Framework, en su navegador web ingrese a
```
http://localhost:8000
```