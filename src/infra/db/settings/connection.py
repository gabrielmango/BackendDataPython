from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .get_envs import get_database_string

class DBConnectionHandler:

    def __init__(self):
        self.__connecting_string = get_database_string()
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connecting_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()