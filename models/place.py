#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
import models
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, String, Float, Column, Integer, Table
from sqlalchemy.orm import relationship

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref='place',
                               cascade='all, delete, delete-orphan')

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")

    else:
        @property
        def reviews(self):
            """
            Returns list of review with pace id
            """
            review = []
            for key, value in models.storage.all().items():
                cls = key.split('.')[0]
                if cls == "Review" and value.place_.id == self.id:
                    review.append(value)
            return (review)

        @property
        def amenities(self):
            """ Getter """
            amenitieslist = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.id == self.amenity_ids:
                    amenitieslist.append(amenity)
            return amenitieslist

        @amenities.setter
        def amenities(self, obj):
            """
            amenities setter
            """
            if type(obj).__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
