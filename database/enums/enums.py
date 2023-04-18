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

class MessageType(enum.Enum):
    bathroom = 'bathroom'
    walk = 'walk'
    breakfast = 'breakfast'
    dinner = 'dinner'
    water = 'water'
    treat = 'treat'