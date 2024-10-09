import requests

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]