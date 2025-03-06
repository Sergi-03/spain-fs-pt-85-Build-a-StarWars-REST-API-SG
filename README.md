# Spain FS PT 85 - Build a Star Wars REST API

Este proyecto consiste en la creación de una API RESTful para gestionar información del universo de Star Wars. La API permite realizar operaciones como obtener información sobre personajes, planetas, naves, especies y vehículos, simulando un sistema de gestión para los elementos del universo de Star Wars.

## Características

- **Obtener personajes**: Accede a detalles sobre personajes del universo de Star Wars.
- **Obtener planetas**: Información sobre los planetas del universo.
- **Obtener naves**: Detalles sobre las naves espaciales presentes en Star Wars.
- **Obtener especies**: Información acerca de las especies presentes en el universo de Star Wars.
- **Obtener vehículos**: Detalles sobre los vehículos en el universo de Star Wars.

## Tecnologías

Este proyecto utiliza las siguientes tecnologías:

- **Node.js**: Plataforma de JavaScript para el backend de la API.
- **Express.js**: Framework minimalista para Node.js utilizado para construir la API RESTful.
- **MongoDB**: Base de datos NoSQL para almacenar los datos de Star Wars.
- **Mongoose**: Librería ODM (Object Data Modeling) para interactuar con MongoDB de manera sencilla.

## Endpoints

La API cuenta con los siguientes endpoints:

- `GET /api/people`: Obtiene la lista de personajes.
- `GET /api/planets`: Obtiene la lista de planetas.
- `GET /api/starships`: Obtiene la lista de naves.
- `GET /api/species`: Obtiene la lista de especies.
- `GET /api/vehicles`: Obtiene la lista de vehículos.

## Uso

### 1. Clona el repositorio
```bash
git clone https://github.com/Sergi-03/spain-fs-pt-85-Build-a-StarWars-REST-API-SG.git
cd spain-fs-pt-85-Build-a-StarWars-REST-API-SG
```

### 2. Instala dependencias
```bash
pipenv install
pipenv shell
```

### 3. Inicia el servidor
```bash
flask run
```

---

## Contacto

Si tienes preguntas o comentarios, no dudes en contactarme en: [ssegarragarcia@gmail.com]
