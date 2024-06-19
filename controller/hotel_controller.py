from model.da.data_access import *
from model.entity import Hotel
from model.tools.decorators import exception_handling


class HotelController:
    hotel_da = DataAccess(Hotel)

    @classmethod
    @exception_handling
    def save(cls, hotel_name, booking_limit, address):
        if (booking_limit == '') or (booking_limit == 'None'):
            booking_limit = None
        hotel = Hotel(hotel_name, booking_limit, address, 0)
        return True, f"saved : {cls.hotel_da.save(hotel)}"

    @classmethod
    @exception_handling
    def edit(cls, id, hotel_name, booking_limit, address, total_rooms):
        if (booking_limit == '') or (booking_limit == 'None'):
            booking_limit = None
        hotel = Hotel(hotel_name, booking_limit, address, int(total_rooms))
        hotel.id = id
        entity = cls.hotel_da.find_by_id(id)
        if entity is None:
            return False, "edit failed entity wasn't found."
        return True, f"edited : {entity}\nTo : {cls.hotel_da.edit(hotel)}"

    @classmethod
    @exception_handling
    def remove(cls, id):
        hotel = cls.hotel_da.find_by_id(id)
        if hotel is None:
            return False, "remove failed entity wasn't found."
        return True, f"removed : {cls.hotel_da.remove(hotel)}"

    @classmethod
    @exception_handling
    def find_all(cls):
        entity_list = cls.hotel_da.find_all()
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        entity_list = cls.hotel_da.find_by_id(id)
        if not entity_list:
            return False, []
        return True, entity_list