from flask import Blueprint, request, jsonify
from database.db import db
from database.models.models import Groups, User
from utils import get_creator

groups = Blueprint('groups', __name__)

@groups.route("/group/users", methods=['POST'])
def fetch_group_users():
    request_json = request.get_json()
    name = request_json["name"]

    get_group = db.session.query(Groups).filter(Groups.name == name).all()
    print(get_group)
    return jsonify(test="details")

@groups.route("/group/create", methods=['POST'])
def group_create():
    request_json = request.get_json()
    name = request_json["name"]
    user = request_json["user"]
    pet_type = request_json["pet_type"]

    group = Groups(name=name, user=user, pet_type=pet_type, user_type="owner")
    db.session.add(group)
    db.session.commit()

    return jsonify(success="group added!")

@groups.route("/groups", methods=['POST'])
def fetch_user_groups():
    request_json = request.get_json()
    user = request_json["user"]

    groups = db.session.query(Groups, User).filter(Groups.user == user).all()

    data = []
    for group in groups:
        creator = group[1].username
        if group[0].user_type != 'owner':
            creator = get_creator(db, group)

        g = {
            "id": group[0].id,
            "name": group[0].name,
            "createdBy": creator,
            "userType": group[0].user_type.name,
            "petType": group[0].pet_type.name,
            "created": group[0].created,
        }
        data.append(g)

    return jsonify(groups=data)

