import enum
from sqlalchemy import Enum

class PetTypes(enum.Enum):
    dog = 'dog'
    cat = 'cat'
    fish = 'fish'
    turtle = 'turtle'
    hamster = 'hamster'

class UserTypes(enum.Enum):
    member = 'member'
    admin = 'admin'
    owner = 'owner'