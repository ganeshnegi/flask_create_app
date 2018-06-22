
import json
import pytest
import random

from project import db
from project.models.user import User

@pytest.fixture(scope="module")
def new_user(client):
    user = User(email="ganesh.negi@3pillarglobal.com", password="login@123", first_name="ganesh", last_name="negi")
    db.session.add(user)
    db.session.commit()
    return user

def test_user(client, new_user):
    assert new_user.email == "ganesh.negi@3pillarglobal.com"
    assert new_user.password == "login@123"

def test_user_registration(client):
    data = {
        "email":"ganesh.negi@3pg.com",
        "password":"login@123",
        "first_name":"ganesh",
        "last_name":"negi"
    }
    res=client.post("/auth/register", data=json.dumps(data))
    assert res.status_code == 201

def test_user_registration_invalid_data(client):
    data = {
        "email":"ganesh.negi@3pg.com",
        "first_name":"ganesh",
        "last_name":"negi"
    }
    res=client.post("/auth/register", data=json.dumps(data))
    assert res.status_code == 400

def test_invalid_login(client, new_user):
    res = client.post("/login", data={"email":"ganesh.negi@3pillarglobal.com", "password":"login@1234"})
    assert res.status_code == 400

def test_get_user_by_valid_id(client, new_user):
	url = '/auth/user/{0}'.format(new_user.id)
	res = client.get(url)
	assert res.status_code == 200

def test_get_user_by_invalid_id(client):
	url = '/auth/user/{0}'.format(random.randint(10000,99999))
	res = client.get(url)
	assert res.status_code == 400