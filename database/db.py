from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.app_context().push()

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/pawtytracker'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from database.routes.users import users
from database.routes.groups import groups
from database.routes.details import details
app.register_blueprint(users)
app.register_blueprint(groups)
app.register_blueprint(details)