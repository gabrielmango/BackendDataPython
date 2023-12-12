from src.infra.db.entities.atendimento.atendimento import Atendimento

from sqlalchemy.orm.exc import NoResultFound

class AtendimentoRepository:

    def __init__(self, ConnectionHandler):
        self.__connection_handler = ConnectionHandler

    def select_all(self):
        with self.__connection_handler() as db:
            try:
                data = db.session.query(Atendimento).all()
                return data
            except NoResultFound:
                return None
            except Exception as e:
                db.session.rollback()
                raise e

    def select(self, co_seq_atendimento):
        with self.__connection_handler() as db:
            try:
                data = db.session.query(Atendimento).filter_by(Atendimento.co_seq_atendimento==co_seq_atendimento).all()
                return data
            except NoResultFound:
                return None
            except Exception as e:
                db.session.rollback()
                raise e
    
    def insert(self, data):
        with self.__connection_handler() as db:
            try:
                data_insert = Atendimento(**data)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
    
    def delete(self, co_seq_atendimento, data):
        with self.__connection_handler() as db:
            try:
                data = db.session.query(Atendimento).filter_by(Atendimento.co_seq_atendimento==co_seq_atendimento).update(**date)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e