#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
import uuid
from datetime import datetime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(
        String(60),
        primary_key=True,
        unique=True,
        nullable=False,
        default=str(uuid.uuid4())
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )

    def __init__(self, *args, **kwargs):
        """Initialize an instance of the BaseModel class"""
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if not kwargs or 'id' not in kwargs:
            models.storage.new(self)

    def save(self):
        """Save the current instance to the storage"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)

    def to_dict(self):
        """Return a dictionary representation of the object"""
        obj_dict = self.__dict__.copy()
        if '_sa_instance_state' in obj_dict:
            del obj_dict['_sa_instance_state']
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
