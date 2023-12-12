from src.infra.db.entities.auditavel import Auditavel

from sqlalchemy import Column, Integer, String, Text, Boolean, Numeric, TIMESTAMP

class Caso(Auditavel):
    __tablename__ = 'tb_caso'
    __table_args__ = {'schema': 'public'}

    co_seq_caso = Column(Integer, primary_key=True)
    co_pessoa = Column(Integer, nullable=False)
    co_situacao_caso = Column(Integer, nullable=False)
    co_uuid_2 = Column(String(255))
    co_uuid_3 = Column(String(255))
    co_uuid_4 = Column(String(255))
    no_protocolo = Column(Text)
    fl_caso_restrito = Column(Boolean, default=False, nullable=False)
    vl_renda_individual = Column(Numeric(14, 2))
    vl_renda_familiar = Column(Numeric(14, 2))
    tp_segredo_justica = Column(Numeric(2))
    tp_prioridade = Column(String(60))
    fl_caso_possui_envolvido = Column(Boolean)
    ds_caso = Column(Text)
    co_caso_replicado = Column(Integer)

    def __repr__(self):
        return f"Caso [co_seq_caso={self.co_seq_caso}, co_pessoa={self.co_pessoa}]"