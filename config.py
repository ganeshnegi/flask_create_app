import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	        'sqlite:///' + os.path.join(basedir, 'app.db')

	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEBUG = True

	JWT_SECRET_KEY = 'jwt-secret-key'
	JWT_BLACKLIST_ENABLED = True
 	JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
