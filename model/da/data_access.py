from sqlalchemy import create_engine,and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity.base import Base

username = "root"
password = "12345678"
database_name = "hotel_management_system"

connection_string = f"mysql+pymysql://{username}:{password}@localhost:3306/{database_name}"

if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()


class DataAccess:
    def __init__(self, class_name):
        self.class_name = class_name
        Base.metadata.create_all(bind=engine)

    def save(self, entity):
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def edit(self, entity):
        session.merge(entity)
        session.commit()
        return entity

    def remove(self, entity):
        session.delete(entity)
        session.commit()
        return entity

    def find_all(self):
        entity_list = session.query(self.class_name).all()
        return entity_list

    def find_by_id(self, id):
        entity = session.get(self.class_name, id)
        return entity

    def find_by(self, find_statement):
        entity = session.query(self.class_name).filter(find_statement).all()
        return entity

    def join(self, *entities):
        base_query = session.query(self.class_name)
        for entity in entities:
            base_query = base_query.join(entity)
        return base_query
