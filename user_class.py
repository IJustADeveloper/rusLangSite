from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from flask_login import UserMixin

Base = declarative_base()


class Users(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(80))
    password = Column(String(100))


engine = create_engine('sqlite:///homeworkDB.db')

Base.metadata.create_all(engine)
