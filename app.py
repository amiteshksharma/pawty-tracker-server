from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.db import db, app

from database.models.models import User

db.create_all()
db.session.commit()

@app.route('/', methods=['GET'])
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)