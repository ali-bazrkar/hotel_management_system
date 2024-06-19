from model.da.data_access import *
from model.entity import User, Hotel, Room, Book
from controller import UserController, HotelController, RoomController, BookController
from model.tools.decorators import exception_handling


class GeneralController:
    user_da = DataAccess(User)
    hotel_da = DataAccess(Hotel)
    room_da = DataAccess(Room)
    book_da = DataAccess(Book)

    @classmethod
    def ensure_list(cls, item):
        if not isinstance(item, list):
            return [item]
        return item

    @classmethod
    @exception_handling  # TEST PASSED
    def find_hotel_rooms(cls, hotel_id):
        entity_list = cls.room_da.find_by(Room.hotel_id == hotel_id)
        entity_list = GeneralController.ensure_list(entity_list)
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling
    def find_books_by_user(cls, user_id):
        entity_list = session.query(Book).filter(Book.user_id == user_id).all()
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling  # TEST PASSED
    def find_all_booked_rooms(cls, hotel_id):
        entity_list = cls.book_da.join(Room).filter(Room.hotel_id == hotel_id).all()
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling  # TESTED PASSED
    def find_user_book(cls, user_id):
        entity_list = cls.book_da.find_by(Book.user_id == user_id)
        entity_list = GeneralController.ensure_list(entity_list)
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling  # TESTED PASSED
    def find_user_room(cls, user_id):
        entity_list = cls.room_da.find_by(Room.user_id == user_id)
        entity_list = GeneralController.ensure_list(entity_list)
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling  # TESTED PASSED
    def find_room_book(cls, room_id):
        entity_list = cls.book_da.find_by(Book.room_id == room_id)
        entity_list = GeneralController.ensure_list(entity_list)
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling  # TESTED PASSED
    # Reminder:  this function returns integer not list
    def find_user_rooms_in_hotel(cls, user_id, hotel_id):
        _, user = UserController.find_by_id(user_id)
        if not user:
            return False, "User not found."
        rooms = [book.room for book in user.books if book.room.hotel_id == hotel_id]
        return True, [len(rooms)]

    @classmethod
    @exception_handling  # TESTED PASSED
    def get_room_count(cls, hotel_id):
        _, hotel = HotelController.find_by_id(hotel_id)
        if not hotel:
            return False, "Hotel not found."
        room_count = hotel.rooms
        status, message = HotelController.edit(hotel.id, hotel.hotel_name, hotel.booking_limit, hotel.address,
                                               len(room_count))
        if status:
            return True, f"updated room count for hotel with id {hotel_id}"
        else:
            return False, "an error occurred ['HotelController' issue]"

    @classmethod
    @exception_handling  # TEST PASSED
    def user_on_remove(cls, user_id):
        _, book_list = GeneralController.find_user_book(user_id)
        book_list = GeneralController.ensure_list(book_list)
        if book_list:
            for book in book_list:
                BookController.remove(book.id)
            _, room_list = GeneralController.find_user_room(user_id)
            room_list = GeneralController.ensure_list(room_list)
            if room_list:
                status = 'empty'
                for room in room_list:
                    RoomController.edit(room.id, room.room_number, room.room_type, status, room.hotel_id, room.user_id)
        status, message = UserController.remove(user_id)
        if status:
            return True, f"info from user with id {user_id} and their booking info found and deleted."
        else:
            return False, 'no value was selected'

    @classmethod
    @exception_handling  # TEST PASSED
    def hotel_on_remove(cls, hotel_id):
        _, room_list = GeneralController.find_hotel_rooms(hotel_id)
        room_list = GeneralController.ensure_list(room_list)
        if room_list:
            for room in room_list:
                _, book = GeneralController.find_room_book(room.id)
                book = GeneralController.ensure_list(book)
                if book:
                    BookController.remove(book[0].id)
                RoomController.remove(room.id)
        status, message = HotelController.remove(hotel_id)
        if status:
            return True, f'hote with id {hotel_id} and its associated rooms were deleted'
        else:
            return False, f'an error occurred'

    @classmethod
    @exception_handling  # TEST PASSED
    def room_on_remove(cls, room_id):
        global hotel_id
        _, room = RoomController.find_by_id(room_id)
        room = GeneralController.ensure_list(room)
        if room:
            hotel_id = room[0].hotel_id
            _, book = GeneralController.find_room_book(room_id)
            book = GeneralController.ensure_list(book)
            if book:
                BookController.remove(book[0].id)
            RoomController.remove(room_id)
            status, message = GeneralController.get_room_count(hotel_id)
            if status:
                return status, 'room and its associated books were deleted.'
        return False, 'an error occurred [room was not found]'

    @classmethod
    @exception_handling  # TEST PASSED
    def room_on_save(cls, room_number, room_type, status, hotel_id):
        status, message = RoomController.save(room_number, room_type, status, hotel_id, None)
        GeneralController.get_room_count(hotel_id)
        if status:
            return True, 'room added and hotel room count updated.'


    @classmethod
    @exception_handling  # TEST PASSED
    def book_on_save(cls, start_date, end_date, user_id, room_id):
        _, room = RoomController.find_by_id(room_id)
        room = GeneralController.ensure_list(room)
        if room:
            hotel_id = room[0].hotel_id
            _, booked_room_count = GeneralController.find_user_rooms_in_hotel(user_id, hotel_id)
            hotel = room[0].hotel
            if (hotel.booking_limit is None) or (hotel.booking_limit > booked_room_count[0]):
                status = 'reserved'
                RoomController.edit(room[0].id, room[0].room_number, room[0].room_type, status, room[0].hotel_id, user_id)
                status, message = BookController.save(start_date, end_date, user_id, room_id)
                if status:
                    return status, 'book saved successfully'
            else:
                return False, 'you have reached your hotel booking limit.'
        return False, "an error occurred [room was not found]"

    @classmethod
    @exception_handling  # TEST PASSED
    def book_on_remove(cls, book_id):
        _, book = BookController.find_by_id(book_id)
        book = GeneralController.ensure_list(book)
        if book:
            _, room = RoomController.find_by_id(book[0].room_id)
            room = GeneralController.ensure_list(room)
            if room:
                status = 'empty'
                RoomController.edit(room[0].id, room[0].room_number, room[0].room_type, status, room[0].hotel_id,
                                    None)
                status, message = BookController.remove(book_id)
                if status:
                    return True, 'book was reset and the book room has been back to default setting'
        return False, 'an error occurred [book was not found]'
