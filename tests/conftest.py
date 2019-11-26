import os
import tempfile
from project import create_app, db, migrate, ma, jwt

import pytest

@pytest.fixture(scope='module')
def client():
    app = create_app(config_class='config.TestingConfig')

    client = app.test_client()

    with app.app_context():
        db.init_app(app)
        db.create_all()
        yield client
        db.drop_all()



