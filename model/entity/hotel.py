from model.entity import *


class Hotel(Base):
    __tablename__ = "hotel_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_name = Column(String(20), nullable=False)
    total_rooms = Column(Integer, nullable=False)
    booking_limit = Column(Integer)
    address = Column(String(255), nullable=False)

    # Relation
    rooms = relationship("Room", back_populates="hotel")

    def __init__(self, hotel_name, booking_limit, address, total_rooms=0):
        self.hotel_name = hotel_name
        self.total_rooms = total_rooms
        self.booking_limit = booking_limit
        self.address = address

    def to_dict(self):
        return {'id': self.id,
                'hotel_name': self.hotel_name,
                'booking_limit': self.booking_limit,
                'total_rooms': self.total_rooms,
                'address': self.address}

    @validates('hotel_name')
    def validate_hotel_name(self, key, hotel_name):
        return Validator.hotel_name_validator(hotel_name, "Invalid Hotel Name.")

    @validates('booking_limit')
    def validate_booking_limit(self, key, booking_limit):
        return Validator.digit_validator(booking_limit, "Enter (int>0) or '' (keep it empty) for booking_limit")

    @validates('address')
    def validate_address(self, key, address):
        return Validator.address_validator(address, "Invalid Address.")
