from flask import Blueprint, request, jsonify
from database.db import db
from database.models.models import GroupDetails

events = Blueprint('events', __name__)

@events.route("/events", methods=['POST'])
def get_group_events():
    request_json = request.get_json()
    group_id = request_json["group_id"]

    get_group_events = db.session.query(GroupDetails).filter(GroupDetails.group_id == group_id)

    data = []
    for group in get_group_events.all():
        dict = {
            "title": group.title,
            "event_id": group.event_id,
            "created_by": group.created_by,
            "group_id": group.group_id,
            "description": group.description,
            "created": group.created,
        }
        data.append(dict)

    return jsonify(details=data)

@events.route("/events/create", methods=['POST'])
def create_event():
    request_json = request.get_json()
    group_id = request_json["group_id"]
    title = request_json["title"]
    created_by = request_json["created_by"]
    description = request_json["description"]

    group = GroupDetails(group_id=group_id, title=title, created_by=created_by, description=description)
    db.session.add(group)
    db.session.commit()

    return jsonify(success="Message created!")

