from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from database.routes.users import users
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/pawtytracker'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(users)

db = SQLAlchemy(app)