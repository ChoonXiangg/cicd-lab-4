def test_full_update_project(client):
    r = client.post("/api/users", json={"name": "Paul", "email": "pl@atu.ie", "age": 25, "student_id": "S1234567"})
    user_id = r.json()["id"]
    r = client.post("/api/projects", json={"name": "Name", "description": "Description", "owner_id": user_id})
    assert r.status_code == 201
    project_id = r.json()["id"]
    r = client.put(f"/api/projects/{project_id}", json={"name": "Nam", "description": "Descriptio", "owner_id": user_id})
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Nam"
    assert data["description"] == "Descriptio"
    assert data["owner_id"] == user_id
    r = client.get(f"/api/projects/{project_id}")
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Nam"
    assert data["description"] == "Descriptio"
    assert data["owner_id"] == user_id