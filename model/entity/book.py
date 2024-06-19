from model.entity import *


class Book(Base):
    __tablename__ = "book_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    # Relation
    user_id = Column(Integer, ForeignKey("user_tbl.id"), nullable=False)
    user = relationship("User", back_populates="books")
    room_id = Column(Integer, ForeignKey("room_tbl.id"), nullable=False, unique=True)
    room = relationship("Room", uselist=False, back_populates='book')

    def __init__(self, start_date, end_date, user_id, room_id):
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id
        self.room_id = room_id

    def to_dict(self):
        return {
            'id': self.id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'name': self.user.name,
            'family': self.user.family,
            'room_number': self.room.room_number,
            'room_type': self.room.room_type,
            'hotel_name': self.room.hotel.hotel_name}

