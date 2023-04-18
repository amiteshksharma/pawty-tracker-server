

from database.models.models import Groups, User


def get_creator(db, group):
    return db.session.query(Groups, User).filter(Groups.user_type == 'owner', Groups.id == group[0].id).all()[0][1].username

def get_members_of_group(db, group):
    get_items = db.session.query(Groups, User).filter(Groups.id == group).all()[1]

    members = []
    for item in get_items:
        members.append(item.username)
    
    return members