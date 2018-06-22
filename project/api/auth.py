from flask_jwt_extended import (
    create_access_token, create_refresh_token, get_raw_jwt, jwt_required, jwt_refresh_token_required
)
from flask_restful import Resource, Api
from flask import request, jsonify, Blueprint

from project.models.user import User, BlacklistedToken

login_logout_bp = Blueprint('login-logout', __name__)

# @app.route('/login', methods = ['POST'])
@login_logout_bp.route('/login', methods = ['POST'])
def login():
    if not request.is_json:
        return jsonify({'error':'invalid json data'}), 400

    login_data = request.get_json()

    email = login_data.get('email')
    password = login_data.get('password')
    
    if not all([email, password]):
        return jsonify({'message':'invalid credentials'}), 400

    user = User.find_by_email(email)

    if not user:
        return jsonify({'error':'user not exist with this email'}), 400

    authenticated = user.check_password(password)

    if not authenticated:
        return jsonify({'error':'invalid username/password'}), 400

    access_token = create_access_token(identity=email)
    refresh_token = create_refresh_token(identity = email)
    return jsonify({
        'access_token':access_token,
        'refresh_token':refresh_token
        }), 200


@login_logout_bp.route('/logout', methods=['POST'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blt = BlacklistedToken(jti=jti)
    blt.add()
    return jsonify({'message':'Access Token revoked'}), 204


@login_logout_bp.route('/logout2', methods=['POST'])
@jwt_refresh_token_required
def logout2():
    jti = get_raw_jwt()['jti']
    blt = BlacklistedToken(jti=jti)
    blt.add()
    return jsonify({'message':'Refresh Token revoked'}), 204