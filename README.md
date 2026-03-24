# Task Manager API

Simple **REST API for managing tasks** built with FastAPI and containerized with Docker.

This project demonstrates a basic backend service with a production-like development setup using:

* FastAPI
* Docker
* Docker Compose
* REST API principles

---

## Architecture

Client → FastAPI → In-memory storage (tasks list)

Application runs inside a Docker container and exposes an HTTP API on port **8000**.

---

## Tech Stack

* Python 3.12
* FastAPI
* Uvicorn
* Docker
* Docker Compose

## Project Structure

```
taskmanager
│
├── app
│   ├── main.py
│   ├── routes.py
│   └── models.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
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
GET /health-check
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
POST /tasks
```

Example body:

```
{
  "title": "Buy milk",
  "description": "from supermarket"
}
```

---

### Get All Tasks

```
GET /tasks
```

---

### Get Task By ID

```
GET /tasks/{task_id}
```

---

### Update Task

```
PUT /tasks/{task_id}
```

---

### Delete Task

```
DELETE /tasks/{task_id}
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

## Future Improvements

* PostgreSQL database
* Reverse proxy with Nginx
* HTTPS with Let's Encrypt
* Monitoring with Prometheus and Grafana
