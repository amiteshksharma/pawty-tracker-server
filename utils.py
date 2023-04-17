

from database.models.models import Groups, User


def get_creator(db, group):
    return db.session.query(Groups, User).filter(Groups.user_type == 'owner', Groups.id == group[0].id).all()[0][1].username