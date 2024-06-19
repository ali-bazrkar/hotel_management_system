from model.entity import *


class Room(Base):
    __tablename__ = "room_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_number = Column(String(3), nullable=False)
    room_type = Column(String(20), nullable=False)
    status = Column(String(20), default="empty")  # empty, reserved, fixing

    # Relation
    hotel_id = Column(Integer, ForeignKey("hotel_tbl.id"), nullable=False)
    hotel = relationship("Hotel", back_populates="rooms")
    user_id = Column(Integer, ForeignKey("user_tbl.id"), default=None)
    user = relationship("User", back_populates="rooms")
    book = relationship("Book", uselist=False, back_populates='room')

    def __init__(self, room_number, room_type, status, hotel_id, user_id):
        self.room_number = room_number
        self.room_type = room_type
        self.status = status
        self.hotel_id = hotel_id
        self.user_id = user_id

    def to_dict(self):
        return {'id': self.id,
                'room_number': self.room_number,
                'room_type': self.room_type,
                'status': self.status,
                'user_id': self.user_id}

    @validates('room_number')
    def validate_room_number(self, key, room_number):
        return Validator.numeric_validator(room_number, "Room number should be 'int' maximum 3 characters.")

    @validates('room_type')
    def validate_room_type(self, key, room_type):
        return Validator.hotel_name_validator(room_type, "Invalid Room Type.")
