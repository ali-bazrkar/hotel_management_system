from model.entity import *


class User(Base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    username = Column(String(20), nullable=False, unique=True)  # UNIQUE ERROR HANDLE - (PASSED)
    password = Column(String(20), nullable=False)
    role = Column(String(20), default="guest")

    # Relation
    books = relationship("Book", back_populates="user")
    rooms = relationship("Room", back_populates="user")

    def __init__(self, name, family, username, password, role="guest"):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'family': self.family,
                'username': self.username,
                'password' : self.password,
                'role': self.role.lower()}

    @validates('name')
    def validate_name(self, key, name):
        return Validator.name_validator(name, "Invalid Name.")

    @validates('family')
    def validate_family(self, key, family):
        return Validator.name_validator(family, "Invalid Family.")

    @validates('username')
    def validate_username(self, key, username):
        return Validator.username_validator(username, "Invalid Username (Username can contain _ a-z 0-9 )")

    @validates('password')
    def validate_password(self, key, password):
        return Validator.password_validator(password, "Invalid Password.")