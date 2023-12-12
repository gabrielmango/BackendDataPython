from pprint import pprint

from src.infra.db.settings.base import Base

from sqlalchemy import Column, Integer, String, Boolean, Numeric, DateTime, TIMESTAMP

class Auditavel(Base):
    __abstract__ = True

    sg_projeto_modificador = Column(String(100))
    sg_acao_modificadora = Column(String(100))
    no_end_point_modificador = Column(String(255))
    st_ativo = Column(Boolean, nullable=False)
    dh_criacao = Column(TIMESTAMP)
    dh_alteracao = Column(TIMESTAMP)
    tp_operacao = Column(String(255), nullable=False) 
    nu_versao = Column(Numeric(10), nullable=False)
    co_uuid = Column(String(255), nullable=False)
    co_uuid_1 = Column(String(255))

    def get_auditavel(self):
        pprint(
                sg_projeto_modificador,
                sg_acao_modificadora,
                no_end_point_modificador,
                st_ativo,
                dh_criacao,
                dh_alteracao,
                tp_operacao,
                nu_versao,
                co_uuid,
                co_uuid_1
        )