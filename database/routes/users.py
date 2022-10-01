from flask import Blueprint, request

users = Blueprint('users', __name__)

@users.route("/user/create", methods=['POST'])
def user_create():
    """ create a user in the Users table """
    args = request.args
    print(args)
    print(request)
    return "hello world"