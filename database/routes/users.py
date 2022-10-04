from flask import Blueprint, request, jsonify
from database.db import db
from database.models.models import User

users = Blueprint('users', __name__)

@users.route("/user/create", methods=['POST'])
def user_create():
    """ create a user in the Users table """
    request_json = request.get_json()
    username = request_json["username"]
    email = request_json["email"]
    uid = request_json["uid"]

    user = User(username=username, email=email, uid=uid)
    db.session.add(user)
    db.session.commit()

    return jsonify(success="User added!")