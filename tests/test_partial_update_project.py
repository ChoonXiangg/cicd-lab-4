def test_partial_update_project(client):
    r = client.post("/api/users", json={"name": "Paul", "email": "pl@atu.ie", "age": 25, "student_id": "S1234567"})
    user_id = r.json()["id"]
    r = client.post("/api/projects", json={"name": "Name", "description": "Description", "owner_id": user_id})
    assert r.status_code == 201
    project_id = r.json()["id"]
    r = client.patch(f"/api/projects/{project_id}", json={"name": "Nam"})
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Nam"
    assert data["description"] == "Description"
    assert data["owner_id"] == user_id
    r = client.get(f"/api/projects/{project_id}")
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Nam"
    assert data["description"] == "Description"
    assert data["owner_id"] == user_id