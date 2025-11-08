import pytest 
from fastapi.testclient import TestClient 
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
 
from app.main import app, get_db 
from app.models import Base 
from sqlalchemy.pool import StaticPool
 
TEST_DB_URL = "sqlite+pysqlite:///:memory:" 
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False}, poolclass = StaticPool) 
TestingSessionLocal = sessionmaker(bind=engine, expire_on_commit=False) 
Base.metadata.create_all(bind=engine)

@pytest.fixture 
def client(): 
    def override_get_db(): 
        db = TestingSessionLocal() 
        try: 
            yield db 
        finally: 
            db.close() 
    app.dependency_overrides[get_db] = override_get_db 
    with TestClient(app) as c: 
        # hand the client to the test 
        yield c 
        # --- teardown happens when the 'with' block exits --- 

def test_create_user(client):
    r = client.post("/api/users", json={"name":"Paul","email":"pl@atu.ie","age":25,"student_id":"S1234567"})
    assert r.status_code == 201

def test_put_user(client):
    r = client.post("/api/users", json={"name":"Choon Xiang","email":"yeohcx@outlook.com","age":22,"student_id":"S1234567"})
    r = client.put(f"/api/users/1", json={"name":"Choon Xian","email":"yeohc@outlook.com","age":21,"student_id":"S1234566"})
    assert r.status_code == 200

def test_patch_user(client):
    r = client.post("/api/users", json={"name":"Choon Xiang","email":"yeohcx@outlook.com","age":22,"student_id":"S1234567"})
    r = client.patch(f"/api/users/1", json={"email":"yeohc@outlook.com"})
    assert r.status_code == 200

def test_put_project(client):
    r = client.post("/api/users", json={"name":"Choon Xiang","email":"yeohcx@outlook.com","age":22,"student_id":"S1234567"})
    r = client.post("/api/projects", json={"name":"Name","description":"Description","owner_id":1})
    r = client.put(f"/api/projects/1", json={"name":"Nam","description":"Desciptio","owner_id":1})
    assert r.status_code == 200

def test_patch_project(client):
    r = client.post("/api/users", json={"name":"Choon Xiang","email":"yeohcx@outlook.com","age":22,"student_id":"S1234567"})
    r = client.post("/api/projects", json={"name":"Name","description":"Description","owner_id":1})
    r = client.patch(f"/api/projects/1", json={"description":"Descriptio"})
    assert r.status_code == 200