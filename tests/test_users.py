def test_create_user(client):
    r = client.post("/api/users", json={"name":"Paul","email":"pl@atu.ie","age":25,"student_id":"S1234567"})
    assert r.status_code == 201

def test_put_user(client):
    r = client.post("/api/users", json={"name":"Choon Xiang","email":"yeohcx@outlook.com","age":22,"student_id":"S1234567"})
    user_id = r.json()["id"]
    r = client.put(f"/api/users/{user_id}", json={"name":"Choon Xian","email":"yeohc@outlook.com","age":21,"student_id":"S1234566"})
    assert r.status_code == 200
    assert r.json()["name"] == "Choon Xian"

def test_patch_user(client):
    r = client.post("/api/users", json={"name":"Choon Xiang","email":"yeohcx@outlook.com","age":22,"student_id":"S1234567"})
    user_id = r.json()["id"]
    r = client.patch(f"/api/users/{user_id}", json={"email":"yeohc@outlook.com"})
    assert r.status_code == 200
    assert r.json()["email"] == "yeohc@outlook.com"
    assert r.json()["name"] == "Choon Xiang"

def test_put_project(client):
    r = client.post("/api/users", json={"name":"Choon Xiang","email":"yeohcx@outlook.com","age":22,"student_id":"S1234567"})
    user_id = r.json()["id"]
    r = client.post("/api/projects", json={"name":"Name","description":"Description","owner_id":user_id})
    project_id = r.json()["id"]
    r = client.put(f"/api/projects/{project_id}", json={"name":"Nam","description":"Desciptio","owner_id":user_id})
    assert r.status_code == 200
    assert r.json()["name"] == "Nam"

def test_patch_project(client):
    r = client.post("/api/users", json={"name":"Choon Xiang","email":"yeohcx@outlook.com","age":22,"student_id":"S1234567"})
    user_id = r.json()["id"]
    r = client.post("/api/projects", json={"name":"Name","description":"Description","owner_id":user_id})
    project_id = r.json()["id"]
    r = client.patch(f"/api/projects/{project_id}", json={"description":"Descriptio"})
    assert r.status_code == 200
    assert r.json()["description"] == "Descriptio"
    assert r.json()["name"] == "Name"