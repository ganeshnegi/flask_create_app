
import json
import pytest

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
    print("-----------------", res.status_code)
    assert res.status_code == 201

def test_invalid_login(client, new_user):
    res = client.post("/login", data={"email":"ganesh.negi@3pillarglobal.com", "password":"login@1234"})
    print("-----------------", res.status_code)
    assert res.status_code == 400



