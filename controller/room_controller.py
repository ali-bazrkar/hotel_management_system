from model.da.data_access import *
from model.entity import Room
from model.tools.decorators import exception_handling


class RoomController:
    room_da = DataAccess(Room)

    @classmethod
    @exception_handling
    def save(cls, room_number, room_type, status, hotel_id, user_id):
        room = Room("{:03}".format(int(room_number)), room_type, status, hotel_id, user_id)
        return True, f"saved : {cls.room_da.save(room)}"

    @classmethod
    @exception_handling
    def edit(cls, id, room_number, room_type, status, hotel_id, user_id):
        room = Room("{:03}".format(int(room_number)), room_type, status, hotel_id, user_id)
        room.id = id
        entity = cls.room_da.find_by_id(id)
        if entity is None:
            return False, "edit failed entity wasn't found."
        return True, f"edited : {entity}\nTo : {cls.room_da.edit(room)}"

    @classmethod
    @exception_handling
    def remove(cls, id):
        room = cls.room_da.find_by_id(id)
        if room is None:
            return False, "remove failed entity wasn't found."
        return True, f"removed : {cls.room_da.remove(room)}"

    @classmethod
    @exception_handling
    def find_all(cls):
        entity_list = cls.room_da.find_all()
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        entity_list = cls.room_da.find_by_id(id)
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling
    def find_empty_rooms_by_hotel(cls, hotel_id):
        entity_list = cls.room_da.find_by(and_(Room.hotel_id == hotel_id, Room.status == 'empty'))
        if not entity_list:
            return False, []
        return True, entity_list
