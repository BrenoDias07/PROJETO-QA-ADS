import requests

def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "userId" in data[0]