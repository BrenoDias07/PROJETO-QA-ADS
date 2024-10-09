import requests

def test_update_post():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    payload = {
        'id': 1,
        'title': 'updated title',
        'body': 'updated body',
        'userId': 1
    }

    response = requests.put(url, json=payload)
    assert response.status_code == 200

    response_json = response.json()
    assert response_json['title'] == 'updated title'
    assert response_json['body'] == 'updated body'