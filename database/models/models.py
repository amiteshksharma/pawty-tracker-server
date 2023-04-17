from sqlalchemy import Enum, ForeignKey, UniqueConstraint
from database.db import db
import time
import uuid

from database.enums.enums import PetTypes, UserTypes

"""
The user table that will contain all information related to the user
  - uid: primary key, non-nullable unique id
  - username: non-nullable, username for the user
  - email: non-nullable, email associated to user
  - created: non-nullable, time when user is created
"""
class User(db.Model):
    uid = db.Column(db.String(30), primary_key=True, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(30), primary_key=True, nullable=False)
    created = db.Column(db.Integer, nullable=False)

    def __init__(self, uid, username, email):
        self.uid = uid
        self.username = username
        self.email = email
        self.created = time.time()

"""
The groups table that will contain all information related to a group
  - id: primary key, non-nullable unique id
  - name: primary key, non-nullable name of group
  - user: foreign key, user who created group
  - user_type: non-nullable, Enum, either member, admin or owner
  - pet_type: non-nullable, Enum, type of pet
  - created: non-nullable, time when group is created
"""
class Groups(db.Model):
    id = db.Column(db.String(64), primary_key=True, nullable=False)
    name = db.Column(db.String(64), primary_key=True, nullable=False)
    user = db.Column(db.String(30), ForeignKey("user.uid"))
    user_type = db.Column(Enum(UserTypes), nullable=False)
    pet_type = db.Column(Enum(PetTypes), nullable=False)
    created = db.Column(db.Integer, nullable=False)

    def __init__(self, name, user, user_type, pet_type):
        self.id = uuid.uuid4().hex
        self.name = name
        self.user = user
        self.user_type = user_type
        self.pet_type = pet_type
        self.created = time.time()