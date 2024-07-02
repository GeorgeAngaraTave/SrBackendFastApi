
# Prueba Técnica Sr Backend - Lizit

Proyecto en FastAPI usando python 3.10 y sqlalchemy y docker(obligatorio)


# Descripción
Este sistema, describe el uso y puesta a punto de una **Api rest** usando [**Python**](https://www.python.org/downloads/) y [**FastAPI**](https://fastapi.tiangolo.com/)

![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)


## Objetivo
El objetivo es crear dos endpoint para la entidad "items", un endpoint para crear un nuevo item
y otro para listar los items creados,
De acuerdo a la arquitectura del proyecto, las capas se comunican de la siguiente manera:
- En routers, estará la definición propiamente del endpoint el cual llamará a una función del
servicio (usa los esquemas para indicar la estructura del body y de la respuesta)
- En servicio, es una capa intermedia que instancia la implementación correspondiente, y llama
la funcionalidad específica que realizará
la acción en base de datos
- En repositorio, recibe el esquema del request lo convierte al modelo


## Requisitos

- [**Python**](https://www.python.org/downloads/) 3.10.x
- [**virtualenv**](https://virtualenv.pypa.io/en/stable/) (Recomendado)
- [**Docker Desktop**](https://hub.docker.com/)

## Recomendaciones
Para tener la facilidad de manejar multiples versiones de python, instalar y configurar el paquete [**pyenv**](https://github.com/pyenv/pyenv), para windows sería [**pyenv-win**](https://github.com/pyenv-win/pyenv-win)

### Explicación  instalación
**Harvey in Coding:** [_Canal youtube_](https://www.youtube.com/watch?v=aF0Ml39oRrE&t=740s)


## Instalación de este repositorio
Clonar este repositorio y alojarlo en una carpeta conveniente.

    git clone https://github.com/

Se recomienda usar [**virtualenv**](https://virtualenv.pypa.io/en/stable/) para desarrollo y pruebas.


## Activar virtualenv en entornos Windows

```sh
python -m virtualenv env
vanv\Scripts\activate

```

Otra forma:

```sh
python -m venv env
env\Scripts\activate

```
## Desactivar virtualenv en entornos Windows

```sh
deactivate
```


## Instalar las dependencias
Una vez dentro del entorno, instalar las dependencias:

```sh
(env) $ pip install -r requirements.txt
```
Otra forma:

```sh
python -m pip install -r requirements.txt
```

# Construir e iniciar el contenedor de Docker
Corre el siguiente comando en tu terminal para construir e iniciar el contenedor de [**Docker**](https://hub.docker.com/)

```sh
docker-compose up --build
```

# Iniciando el servidor web
A continuación se describen algunas configuraciones para iniciar el servidor web.

>La direccion y el puerto por defecto es: [**http://localhost:8000**](http://localhost:8000)

Verificar servicos

>Docimentación: [**localhost:8000/docs**](localhost:8000/docs)



# Estructura del Proyecto
```text
/
├── app
│ ├── __init__.py
│ ├── main.py
│ └── routers
│ │ ├── __init__.py
│ │ ├── items.py
│ └── services
│ │ ├── __init__.py
│ │ ├── items_service.py
│ └── models
│ ├── __init__.py
│ └── items.py
│ └── schemas
│ ├── __init__.py
│ └── items_schemas.py
│ └── repositories
│ │ ├── __init__.py
│ │ └── item_repository
```
