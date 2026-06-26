from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import TaskModel
from sqlalchemy.pool import StaticPool
from app.main import app
from app.database import get_db

engine_testing = create_engine(
    "sqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool
)

Tests_Local_Session = sessionmaker(engine_testing)

Base.metadata.create_all(engine_testing)

def get_test_db():
    db_tests = Tests_Local_Session()
    try:
      yield db_tests
    finally:
      db_tests.close()

app.dependency_overrides[get_db] = get_test_db

client = TestClient(app)

def test_create_task():
   response = client.post("/api/v1/tasks", json={"title": "create task"})
   assert response.status_code == 201
   assert response.json()["title"] == "create task"


def test_get_tasks():
    client.post("/api/v1/tasks", json={"title": "get tasks"})
    response = client.get("/api/v1/tasks")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_task():
   task_id = client.post("/api/v1/tasks", json={"title": "test"}).json()["id"]
   response = client.get(f"/api/v1/tasks/{task_id}")
   assert response.status_code == 200
   assert (response.json()["id"]) == task_id

def test_get_task_not_found():
   response = client.get("/api/v1/tasks/id-not-exists")
   assert response.status_code == 404

def test_update_task():
   task_id = client.post("/api/v1/tasks", json={"title": "test", "completed": False}).json()["id"]
   status_updated = {"title": "updated", "completed": True}
   task_updated = client.put(f"/api/v1/tasks/{task_id}", json=status_updated).json()["completed"]
   response = client.get(f"/api/v1/tasks/{task_id}")
   assert response.status_code == 200
   assert response.json()["completed"] == task_updated

def test_delete_task():
   task_id = client.post("/api/v1/tasks", json={"title": "test"}).json()["id"]
   deleted_task = client.delete(f"/api/v1/tasks/{task_id}")
   assert deleted_task.status_code == 204



   




