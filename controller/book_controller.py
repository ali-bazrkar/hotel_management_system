from model.da.data_access import *
from model.entity import Book
from model.tools.decorators import exception_handling


class BookController:
    book_da = DataAccess(Book)

    @classmethod
    @exception_handling
    def save(cls, start_date, end_date, user_id, room_id):
        book = Book(start_date, end_date, user_id, room_id)
        return True, f"saved : {cls.book_da.save(book)}"

    @classmethod
    @exception_handling
    def edit(cls, id, start_date, end_date, user_id, room_id):
        book = Book(start_date, end_date, user_id, room_id)
        book.id = id
        entity = cls.book_da.find_by_id(id)
        if entity is None:
            return False, "edit failed entity wasn't found."
        return True, f"edited : {entity}\nTo : {cls.book_da.edit(book)}"

    @classmethod
    @exception_handling
    def remove(cls, id):
        book = cls.book_da.find_by_id(id)
        if book is None:
            return False, "remove failed entity wasn't found."
        return True, f"removed : {cls.book_da.remove(book)}"

    @classmethod
    @exception_handling
    def find_all(cls):
        entity_list = cls.book_da.find_all()
        if not entity_list:
            return False, []
        return True, entity_list

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        entity_list = cls.book_da.find_by_id(id)
        if not entity_list:
            return False, []
        return True, entity_list

