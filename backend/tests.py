import json

import requests


def get_user(ident=1):
    user = requests.get(f"http://10.82.213.254/users/get/{ident}")
    print(f"users/get/[id] - {json.dumps(json.loads(user.text), indent=4)}\n\n")


def get_users():
    users = requests.get(f"http://10.82.213.254/users/get")
    print(f"users/get - {json.dumps(json.loads(users.text), indent=4)}\n\n")


def put_user():
    url = "http://10.82.213.254/users/put"
    data = {
        "comments_id": [1, 2],
        "name_id": 2,
        "phone": "88005553535",
        "rating": 4.2,
        "user_type": 2,
        "mail": "alexabdelnur@yandex.ru"
    }
    resp = requests.put(url, json=data)
    print(f"/users/put {json.loads(resp.text)}\n\n")


def delete_user(ident):
    url = f"http://10.82.213.254/users/delete/{ident}"
    resp = requests.delete(url)
    print(f"/users/delete/[id] - {json.dumps(json.loads(resp.text), indent=4)}\n\n")


def put_name():
    url = "http://10.82.213.254/name/put"
    data = {
        "firstname": "Alex",
        "lastname": "Abdelnur",
        "fathername": "Fateh"
    }
    resp = requests.put(url, json=data)
    print(f"/name/put - {json.dumps(json.loads(resp.text), indent=4)}\n\n")


def get_city(ident=1):
    url = f"http://10.82.213.254/cities/get/{ident}"
    resp = requests.get(url)
    print(f"/cities/get - {json.dumps(json.loads(resp.text), indent=4)}\n\n")


if __name__ == "__main__":
    get_user(2)
    delete_user(2)
    put_user()
    get_users()
    get_city(1)
    # put_name()
