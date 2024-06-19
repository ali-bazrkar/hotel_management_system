from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, validates

from model.tools.validator import Validator

from model.entity.base import Base
from model.entity.user import User
from model.entity.hotel import Hotel
from model.entity.room import Room
from model.entity.book import Book
