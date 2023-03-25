#!/usr/bin/python3
""" New db engine """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """ DB STORAGE class """
    __engine = None
    __session = None

    def __init__(self):
        """ Self declaration """
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ CALLS self on all """
        objs = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = f"{cls.__name__}.{obj.id}"
                objs[key] = obj
        else:
            for cls in Base.__subclasses__():
                query = self.__session.query(cls).all()
                for obj in query:
                    key = f"{cls.__name__}.{obj.id}"
                    objs[key] = obj
        return objs

    def new(self, obj):
        """ Creates a new instance"""
        self.__session.add(obj)

    def save(self):
        """ Saves the new db """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes the new db """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads the new db """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
