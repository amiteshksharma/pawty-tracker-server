from database.db import db
import time
import uuid

"""
The user table that will contain all information related to the user
  - uid: primary key, non-nullable unique id
  - username: non-nullable, username for the user
  - email: non-nullable, email associated to user
  - created: non-nullable, time when user is created
"""
class User(db.Model):
    uid = db.Column(db.String(30), primary_key=True, nullable=False)
    email = db.Column(db.String(64), primary_key=True, nullable=False)
    username = db.Column(db.String(30), nullable=False)
    created = db.Column(db.Integer, nullable=False)

    def __init__(self, uid, username, email):
        self.uid = uid
        self.username = username
        self.email = email
        self.created = time.time()