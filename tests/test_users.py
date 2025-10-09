# tests/test_users.py
import pytest

def user_payload(uid=1, name="Paul", email="pl@atu.ie", age=25, sid="S1234567"):
    return {"user_id": uid, "name": name, "email": email, "age": age, "student_id": sid}

def test_create_user_ok(client):
    r = client.post("/api/users", json=user_payload())
    assert r.status_code == 201
    data = r.json()
    assert data["user_id"] == 1
    assert data["name"] == "Paul"

def test_duplicate_user_id_conflict(client):
    client.post("/api/users", json=user_payload(uid=2))
    r = client.post("/api/users", json=user_payload(uid=2))
    assert r.status_code == 409 # duplicate id -> conflict
    assert "exists" in r.json()["detail"].lower()

@pytest.mark.parametrize("bad_sid", ["BAD123", "s1234567", "S123", "S12345678"])
def test_bad_student_id_422(client, bad_sid):
    r = client.post("/api/users", json=user_payload(uid=3, sid=bad_sid))
    assert r.status_code == 422 # pydantic validation error

def test_get_user_404(client):
    r = client.get("/api/users/999")
    assert r.status_code == 404

def test_delete_then_404(client):
    client.post("/api/users", json=user_payload(uid=10))
    r1 = client.delete("/api/users/10")
    assert r1.status_code == 204
    r2 = client.delete("/api/users/10")
    assert r2.status_code == 404

#Test update_user, returns 200 on success and 404 if id not found
def test_update_user_ok(client):
    client.post("/api/users", json=user_payload()) 
    r = client.put("/api/users/update/1", json=user_payload(name="ChoonXiang", email="g00425056@atu.ie", age=22, sid="S1234567")) 
    assert r.status_code == 200 
    data = r.json() 
    assert data["name"] == "ChoonXiang" 
    assert data["email"] == "g00425056@atu.ie"
    assert data["age"] == 22 
    assert data["student_id"] == "S1234567"
    r = client.put("/api/users/update/999", json=user_payload(name="ChoonXiang"))
    assert r.status_code == 404

#Test creating a bad email, returns 422
@pytest.mark.parametrize("bad_email", ["g00425056@atu", "g00425056@.ie", "g00425056@com", "g00425056@"]) 
def test_bad_email_422(client, bad_email): 
    r = client.post("/api/users", json=user_payload(uid=3, sid=bad_email)) 
    assert r.status_code == 422