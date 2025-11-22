# Docker Zero To Container
## API Flask + Postgres + Frontend Nginx
### Koki Duré – DevFest 2025

Este proyecto es una demo práctica para aprender cómo levantar una arquitectura completa usando Docker y docker-compose, en menos de una hora.

#### Incluye:
- API en Python + Flask
- Base de datos Postgres
- Frontend estático servido con Nginx
- Todo corriendo en contenedores separados
- Ideal para aprender, practicar y romper sin miedo 😎

#### 1. Requisitos
Antes de empezar, necesitás tener instalado:

✔ Git: https://git-scm.com/downloads

Verificar con: `git --version`

✔ Docker Desktop

https://www.docker.com/products/docker-desktop

- Requiere: WSL2 activado
  / Virtualización habilitada (casi siempre viene activada)

✔ Windows 10/11 (64 bits)

✔ (Opcional recomendado) VS Code, extensiones Docker y Python

Para verificar que Docker funciona:

`docker version`

`docker run hello-world`


Si todo eso anda, estás listo 💪

#### 2. Clonar este repositorio
`git clone https://github.com/kokidure/docker-zero-to-container.git`

`cd docker-zero-to-container`

#### 3. Estructura y servicios
- web: API Flask
- db: Postgres + volumen persistente
- frontend: Nginx sirviendo HTML/CSS/JS

#### 4. Cómo levantar toda la arquitectura
Desde la raíz del proyecto:

- `docker-compose up --build`


Esto va a:

- Construir la imagen del backend (Flask)

- Levantar Postgres + volumen de datos

- Construir la imagen del frontend (Nginx)

- Crear una red interna entre los contenedores

- Exponer los puertos al host

- Cuando veas logs de Flask, Postgres y Nginx…
ya estás 👌

#### 5. Cómo probar que funciona
✔ API Flask

Abrí en el navegador:

http://localhost:5000/

http://localhost:5000/db

✔ Frontend (Nginx)

Abrí:

http://localhost:8080/

Ahí vas a ver una web simple que llama a la API Flask y muestra:

- Estado de la API

- Hora desde Postgres

#### 6. Comandos útiles

- Listar contenedores activos: `docker ps`

- Ver logs del backend: `docker logs -f flask_app`

- Apagar todo: `docker-compose down`

- Eliminar contenedores + imágenes + volúmenes: `docker system prune -a`

#### 7. ¿Qué aprendés con esta demo?

- Cómo empacar un backend Flask en Docker.

- Cómo correr una base de datos real dentro de un contenedor.

- Cómo servir un frontend con Nginx.

- Cómo conectar múltiples servicios con Docker Compose.

- Cómo persistir datos con volúmenes.

- Cómo estructurar una arquitectura realista y moderna.

#### 8. ¿Y ahora qué? (Siguientes pasos recomendados)

Si querés seguir aprendiendo:
 
- Crear nuevos endpoints en Flask.

- Mostrar esos datos en el frontend.

- Levantar múltiples instancias del backend.

- Probar Dev Containers (VS Code).

- Llevar esta misma arquitectura a Kubernetes (conceptual o demo).