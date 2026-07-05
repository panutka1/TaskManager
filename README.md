# Task Manager API

Simple **REST API for managing tasks** built with FastAPI and containerized with Docker.

(For Kubernetes deployment see repo TaskManager_devops: 
https://github.com/panutka1/TaskManager_devops
)

This project demonstrates a basic backend service with a production-like development setup using:

* FastAPI
* Docker
* Docker Compose
* REST API principles
* PostgreSQL
* Alembic
* Pytest

---

## Architecture

Client → FastAPI → PostgreSQL

Application runs inside a Docker container and exposes an HTTP API on port **8000**.

---

## Tech Stack

* Python 3.12
* FastAPI
* Uvicorn
* Docker
* Docker Compose
* PostgreSQL
* Alembic
* Pytest

## Project Structure

```
taskmanager
|
|- app
|   |- main.py
|   |- routes.py
|   |- models.py
|   |- database.py
|
|- migrations/
|- tests
|   |-test_tasks.py
|
|- Dockerfile
|- docker-compose.yml
|- requirements.txt
|- README.md
```

---

## Running the Application

### 1. Clone repository

```
git clone <repo-url>
cd taskmanager
```

### 2. Run with Docker Compose

```
docker compose up --build
```

The API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

## API Endpoints

### Health Check

```
GET /api/v1/health-check
```

Response:

```
{
  "status": "ok"
}
```

---

### Create Task

```
POST /api/v1/tasks
```

---

### Get All Tasks

```
GET /api/v1/tasks
```

---

### Get Task By ID

```
GET /api/v1/tasks/{task_id}
```

---

### Update Task

```
PUT /api/v1/tasks/{task_id}
```

---

### Delete Task

```
DELETE /api/v1/tasks/{task_id}
```

---

## Development

Start the application:

```
docker compose up
```

Stop containers:

```
docker compose down
```

---

## Tests

Run tests:

```
cd TaskManager

pytest tests/

```

## Future Improvements

* Reverse proxy with Nginx
* HTTPS with Let's Encrypt
* Monitoring with Prometheus and Grafana
