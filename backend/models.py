import json

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128))
    description_id = Column(Integer)
    comments_id = Column(String)
    city_id = Column(Integer)
    place_id = Column(Integer)
    rating = Column(Float)


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128))

    def __str__(self):
        return json.dumps({"id": self.id,
                           "name": self.name})


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name_id = Column(Integer)
    comments_id = Column(String(1024))
    mail = Column(String(64))
    phone = Column(String(64))
    rating = Column(Float)
    user_type = Column(Integer)

    def __str__(self):
        return json.dumps({"id": self.id,
                           "name_id": self.name_id,
                           "comments_id": json.loads(self.comments_id),
                           "mail": self.mail,
                           "phone": self.phone,
                           "rating": self.rating,
                           "user_type": self.user_type,
                           "status": "Success",
                           "code": 200}, indent=4)


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    header = Column(String(128))
    content = Column(String(512))
    rating = Column(Float)


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128))
    date = Column(String(16))
    time = Column(String(8))
    description = Column(String(1024))
    photo = Column(String(1024))
    link = Column(String(1024))
    age = Column(String(8))


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    header = Column(String(128))
    description = Column(String(1024))
    image = Column(String(1024))
    comments = Column(String(1024))
    schedule = Column(String(1024))


class Description(Base):
    __tablename__ = "descriptions"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(1024))
    audio = Column(String(1024))
    photo = Column(String(1024))


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    coordinates = Column(String(64))
    address = Column(String(256))


class Name(Base):
    __tablename__ = "names"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(64))
    lastname = Column(String(64))
    fathername = Column(String(64))
