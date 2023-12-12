from src.infra.db.entities.auditavel import Auditavel

from sqlalchemy import Column, Integer, String, Boolean


class Pessoa(Auditavel):
    __tablename__ = 'tb_pessoa'
    __table_args__ = {'schema': 'public'}
    
    co_seq_pessoa = Column(Integer, primary_key=True)
    no_pessoa = Column(String(100), nullable=False)
    no_social_pessoa = Column(String(100))
    fl_nome_social_pessoa = Column(Boolean)
    co_profissao_pessoa = Column(Integer)
    no_outra_profissao_pessoa = Column(String(100))
    co_uuid_3 = Column(String(255))
    co_faixa_renda_pessoa = Column(Integer)
    ds_tipo_pessoa = Column(String(60))
    ds_vinculo_empregaticio_pessoa = Column(String(30))
    fl_trabalhador_autonomo_pessoa = Column(Boolean)
    fl_possui_contrato_pessoa = Column(Boolean)
    fl_acompanhar_atend_pessoa = Column(Boolean)
    no_lingua_falada_pessoa = Column(String(60))
    id_assisted_sgc = Column(Integer)
    fl_situacao_rua = Column(Boolean, nullable=False, default=False)
    fl_trajetoria_rua = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
            return f"Pessoa [co_seq_pessoa={self.co_seq_pessoa}, no_pessoa={self.no_pessoa}]"