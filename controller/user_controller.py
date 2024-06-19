from model.da.data_access import *
from model.entity import User
from model.tools.decorators import exception_handling


class UserController:
    user_da = DataAccess(User)

    @classmethod
    @exception_handling
    def save(cls, name, family, username, password, role):
        user = User(name, family, username, password, role)
        return True, f"saved : {cls.user_da.save(user)}"

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, username, password, role):
        user = User(name, family, username, password, role)
        user.id = id
        entity = cls.user_da.find_by_id(id)
        if entity is None:
            return False, "edit failed entity wasn't found."
        return True, f"edited: {entity}\nTo : {cls.user_da.edit(user)}"

    @classmethod
    @exception_handling
    def remove(cls, id):
        user = cls.user_da.find_by_id(id)
        if user is None:
            return False, "remove failed entity wasn't found."
        return True, f"removed : {cls.user_da.remove(user)}"

    @classmethod
    @exception_handling
    def find_all(cls):
        entity_list = cls.user_da.find_all()
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        entity_list = cls.user_da.find_by_id(id)
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        entity_list = cls.user_da.find_by(User.username == username)
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        entity_list = cls.user_da.find_by(and_(User.username == username, User.password == password))
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling
    def find_by_guest(cls):
        entity_list = cls.user_da.find_by(User.role == 'guest')
        if not entity_list:
            return False, []
        return True, entity_list