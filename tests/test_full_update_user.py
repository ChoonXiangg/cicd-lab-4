def test_full_update_user(client):
    r = client.post("/api/users", json={"name": "Paul", "email": "pl@atu.ie", "age": 25, "student_id": "S1234567"})
    assert r.status_code == 201
    user_id = r.json()["id"]
    r = client.put(f"/api/users/{user_id}", json={"name": "Pau", "email": "p@atu.ie", "age": 26, "student_id": "S1234568"})
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Pau"
    assert data["email"] == "p@atu.ie"
    assert data["age"] == 26
    assert data["student_id"] == "S1234568"
    r = client.get(f"/api/users/{user_id}")
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Pau"
    assert data["email"] == "p@atu.ie"
    assert data["age"] == 26
    assert data["student_id"] == "S1234568"
