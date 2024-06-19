
from model.tools.decorators import exception_handling
from model.da.data_access import *
from controller import *

from controller.general_controller import GeneralController
from model.entity import *


# CREATE PASSED
#UserController.edit(1,"name", "family", "username", "password", "guest")
#_,slist = HotelController.find_all()
#print(slist)

#HotelController.save("hotel name 1", 2, 'tehran enghelab NAme, street')



# UserController.save("username2", "password", "guest")
# GuestController.save("name", "family", None, None, 1)
# GuestController.save("name", "family", None, None, 2)
# HotelController.save("hotel-name1", 2, "address.")
#HotelController.save("hotel-name2", None, "address.")
#RoomController.save("01","Dual-Bed","empty", 1, None)
#RoomController.save("02","Dual-Bed","empty", 1, None)
#RoomController.save("03","Dual-Bed","empty", 1, None)
#RoomController.save("04","Dual-Bed","empty", 1, None)
#RoomController.save("05","Dual-Bed","empty", 1, None)
#RoomController.save("06","Dual-Bed","empty", 1, None)
#RoomController.save("07","Dual-Bed","empty", 1, None)
# RoomController.save("08","Dual Bed","empty", 1, None)
# RoomController.save("07","Dual Bed","empty", 1, None)
# RoomController.save("09","Dual Bed","empty", 1, None)
# RoomController.save("10","Dual Bed","empty", 1, None)
# RoomController.save("11","Dual Bed","empty", 1, None)
# RoomController.save("12","Dual Bed","empty", 1, None)
#RoomController.save("01","Dual Bed","empty", 4, None)
#RoomController.save("02","Dual Bed","empty", 4, None)
#RoomController.save("03","Dual Bed","empty", 4, None)
#RoomController.save("04","Dual Bed","empty", 4, None)
#RoomController.save("05","Dual Bed","empty", 4, None)
# HotelController.hotel_room_count()

#GeneralController.book_on_save("2000-10-10", "2000-10-10", 1, 2)
#GeneralController.book_on_save("2000-10-10", "2000-10-10", 1, 3)
# BookController.save("2000-10-10", "2000-10-10",1, 2)
# BookController.save("2000-10-10", "2000-10-10",1, 3)
# BookController.save("2000-10-10", "2000-10-10",2, 18)
# BookController.save("2000-10-10", "2000-10-10",2, 17)
# BookController.save("2000-10-10", "2000-10-10",2, 16)

# EDIT PASSED
# UserController.edit(1,"username1", "password", "guest")
# GuestController.edit(1, "name", "family", None, None, 1)
# HotelController.edit(1, "hotel-name1", 2, "address2.", None)
# RoomController.edit(18, "09","Dual-Bed","empty", 2, None)

# REMOVE
# BookController.remove(5)
# RoomController.remove(16)
# HotelController.hotel_room_count()
# HotelController.remove(1)
# HotelController.hotel_room_count()
# UserController.remove(1)

# TRUE
# _,a = UserController.find_all()
# print(a)

# _, a = GuestController.find_guest_by_user_id(13)
# print(a)

# print(GuestController.merge_function())


# _,user = UserController.find_by_id(9)
# print(user)


# GuestController.remove(6)
# GuestController.remove(8,)
# UserController.remove(18)


#GeneralController.book_on_save("2000-10-10", "2000-10-10",1, 1)
#b = (RoomController.find_by_id(1))
#print(b)
#a = RoomController.find_all()
#print(a)

#_, hotel = HotelController.find_by_id(1)
#print(hotel.rooms)

#a = GeneralController.find_hotel_rooms(1)
#print(a)

#a = RoomController.find_by_id(11)
#print(a)

#GeneralController.book_on_save('2000-2-2', '2000-2-2', 1, 10)
#GeneralController.book_on_save('2000-2-2', '2000-2-2', 1, 11)
#GeneralController.book_on_save('2000-2-2', '2000-2-2', 1, 12)
#GeneralController.book_on_save('2000-2-2', '2000-2-2', 3, 7)
#_,a = RoomController.find_by_id(1)
#b = a.hotel_id
#print(b)

#GeneralController.book_on_remove(6)
#GeneralController.room_on_save('07', 'dual-bed', 'empty', 4)
#GeneralController.find_user_rooms_in_hotel(1, 1)

#_,a = GeneralController.find_hotel_empty_rooms(1)
#print(a)

#_, a = GeneralController.book_on_save("2000-2-2","2000-2-2",1,4 )
#print(a)

print('ali bazrkar'.capitalize())