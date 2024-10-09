import requests

def test_delete_post():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.delete(url)
    assert response.status_code == 200  # ou 204
