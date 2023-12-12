from src.infra.db.entities.auditavel import Auditavel

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime


class Atendimento(Auditavel):
    __tablename__ = 'tb_atendimento'
    __table_args__ = {'schema': 'public'}
    
    co_seq_atendimento = Column(Integer, primary_key=True)
    co_caso = Column(Integer, nullable=False)
    co_uuid_3 = Column(String(255))
    fl_atendimento_restrito = Column(Boolean, nullable=False, default=False)
    ds_atendimento = Column(Text)
    dh_inicio_atendimento = Column(DateTime)
    dh_fim_atendimento = Column(DateTime)
    co_uuid_4 = Column(String(255))
    no_protocolo = Column(String(100))
    co_uuid_5 = Column(String(255))
    fl_atendimento_por_cooperacao = Column(Boolean)
    tp_atividade_atendimento = Column(String(30))
    co_uuid_6 = Column(String(255))

    def __repr__(self):
        return f"Atendimento [co_seq_atendimento={self.co_seq_atendimento}, co_caso={self.co_caso}]"