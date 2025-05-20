import requests

def test_get_users():
    url = "https://gorest.co.in/public/v2/users"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "name" in data[0]
