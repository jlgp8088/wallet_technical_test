# WALLET - PRUEBA TECNICA

#### Jose Luis Guerrero

## Configuracion

Descargar el repositorio

```sh
$ git clone https://github.com/jlgp8088/wallet_technical_test.git
$ cd wallet_technical_test
```

Crear entorno virtual

```sh
$ python3 -m venv venv
```

Se activa el entorno virtual

```sh
$ source venv/bin/activate
```

Se realiza la instalacion de las dependencias

```sh
(venv)$ pip install -r requirements.txt
```
Nota: `(venv)` al inicio del comando, indica que te encuentras dentro del entorno virtual.

Se ejecuta el proceso de migracion

```sh
(venv)$ ./manage.py makemigrations
(venv)$ ./manage.py migrate
```

Se crea un usuario super administrador

```sh
(venv)$ ./manage.py createsuperuser
```
pedira los siguientes datos

```sh
Username (leave blank to use 'user'):
Email address:
Password:
Password (again):
Superuser created successfully.
```

Se recomienda sembrar la informacion base

```sh
(venv)$ ./manage.py loaddata ./seeds/fees.json
Installed 2 object(s) from 1 fixture(s)
(venv)$ ./manage.py loaddata ./seeds/country.json
Installed 2 object(s) from 1 fixture(s)
(venv)$ ./manage.py loaddata ./seeds/coin.json
Installed 3 object(s) from 1 fixture(s)
```

Se levanta el servidor local

```sh
(venv)$ ./manage.py runserver 
```

## PANEL ADMINISTRATIVO

[Panel administrativo Django](http://localhost:8000/admin)

Se debe ingresar con el usuario super adminsitrador creado durante la configuracion

## DOCUMENTACION

El consumo de las apis se encuentra disponible en el siguiente link

[Documentacion Postman](https://documenter.getpostman.com/view/2sA2rGvf29)



## ESTRUCTURA

```
wallet/
|-- api/   # consumo de apis externas
|   |-- modelos.py
|   |-- vistas.py
|   |-- ...
|-- auth/  # logica de autenticacion y manejo de jwtoken
|   |-- modelos.py
|   |-- vistas.py
|   |-- ...
|-- coins/  # modulo para el manejo de monedas
|   |-- modelos.py
|   |-- vistas.py
|   |-- ...
|-- seeds/  # archivos con infomacion mockup base de datos
|   |-- country.json
|   |-- ...
|-- transaction/  # logica de transacciones fiat y blockchain
|   |-- modelos.py
|   |-- vistas.py
|   |-- ...
|-- users/  # logica de manejo de usuarios y sus propiedades
|   |-- modelos.py
|   |-- vistas.py
|   |-- ...
|-- utils/  # funcionalidades generales 
|   |-- modelos.py
|   |-- vistas.py
|   |-- ...
|-- manage.py
|-- README.md

