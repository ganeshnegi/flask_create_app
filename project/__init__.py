from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()

ma = Marshmallow()
jwt = JWTManager()

def create_app(config_class='config.Config'):
	app = Flask(__name__)
	app.config.from_object(config_class)

	with app.app_context():
		db.init_app(app)
		
	migrate = Migrate(app, db)
	ma = Marshmallow(app)
	jwt = JWTManager(app)

	from .models import user

	from .api import index, auth, post as post_api, user as user_api
	
	app.register_blueprint(index.bp_home)
	app.register_blueprint(auth.login_logout_bp)
	app.register_blueprint(user_api.user_blueprint)

	@jwt.token_in_blacklist_loader
	def check_if_token_in_blacklist(decrypted_token):
		jti = decrypted_token['jti']
		return user.BlacklistedToken.is_jti_blacklisted(jti)

	
	return app

