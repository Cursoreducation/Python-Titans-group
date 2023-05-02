import requests


def test_get_articles_list():
    response = requests.get("http://nginx/api/articles")
    assert response.status_code == 200
    assert response.json()[0].get("id") == 1


def test_create_article():
    response = requests.post("http://nginx/api/articles", json={
        "title": "hello",
        "body": "hello hello hello"
    })
    assert response.status_code == 200
    assert response.json().get("title") == "hello"
    res = requests.delete("http://nginx/api/articles/" + str(response.json().get("id")))
    assert res.status_code == 204