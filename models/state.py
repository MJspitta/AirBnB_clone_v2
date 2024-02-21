#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import Base, BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
        """get list of all related city objects"""
            city_lst = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_lst.append(city)
            return city_lst
