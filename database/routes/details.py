from flask import Blueprint, request, jsonify
from database.db import db
from database.models.models import Groups, User, GroupDetails
from utils import get_creator, get_members_of_group

details = Blueprint('details', __name__)

@details.route("/details", methods=['POST'])
def get_group_messages():
    request_json = request.get_json()
    group_id = request_json["group_id"]

    get_group_details = db.session.query(GroupDetails).filter(GroupDetails.group_id == group_id).all()
    members = get_members_of_group(db, group_id)

    data = []
    for group in get_group_details:
        data.append(group)

    return jsonify(details=data, members=members)

@details.route("/details/create", methods=['POST'])
def fetch_group_users():
    request_json = request.get_json()
    group_id = request_json["group_id"]
    message_type = request_json["message_type"]
    created_by = request_json["created_by"]
    comment = request_json["comment"]

    group = GroupDetails(group_id=group_id, message_type=message_type, created_by=created_by, comment=comment)
    db.session.add(group)
    db.session.commit()

    return jsonify(success="Message created!")

