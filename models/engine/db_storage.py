#!/usr/bin/python3
''' Module defining DBStorage class '''

import MySQLdb
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                        user='hbnh_dev', passwd='hbnh_dev_pwd',
                        host='localhost', db='hbnb_dev_db'),
                        pool_pre_ping=True)

    def all(self, cls=None):
        self.__session = sessionmaker(bind=engine)
