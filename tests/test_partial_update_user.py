def test_partial_update_user(client):
    r = client.post("/api/users", json={"name": "Paul", "email": "pl@atu.ie", "age": 25, "student_id": "S1234567"})
    assert r.status_code == 201
    user_id = r.json()["id"]
    r = client.patch(f"/api/users/{user_id}", json={"name": "Pau"})
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Pau"
    assert data["email"] == "pl@atu.ie"
    assert data["age"] == 25
    assert data["student_id"] == "S1234567"
    r = client.get(f"/api/users/{user_id}")
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Pau"
    assert data["email"] == "pl@atu.ie"
    assert data["age"] == 25
    assert data["student_id"] == "S1234567"
