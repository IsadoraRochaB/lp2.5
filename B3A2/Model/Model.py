from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DECIMAL, DateTime

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)

    comentario = relationship("Comentario",backref='Usuario', lazy=True)
    atividade = relationship("Atividade",backref='Usuario', lazy=True)
    curtida = relationship("Curtida",backref='Usuario', lazy=True)

    def __repr__(self):
        return f'Usuario {self.nome}'

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()

class Atividade(Base):
    __tablename__ = 'atividade'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    inicio = Column(DateTime(255), unique=True, nullable=False)
    fim = Column(DateTime(255), unique=True, nullable=False)
    quilometros = Column(DECIMAL(10,2), nullable=False)
    tipo = Column(String(255), nullable=False)
    local = Column(String(255), nullable=False)

    comentario = relationship("Comentario",backref='Atividade', lazy=True)

    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", backref="Atividade")

    def __repr__(self):
        return f'Atividade {self.nome}'

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    comentario = Column(String(255), nullable=True)

    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", backref="Comentario")

    atividade_id = Column(Integer, ForeignKey('atividade.id'))
    atividade = relationship("Atividade", backref="Comentario")


    def __repr__(self):
        return f'Comentario {self.comentario}'

class Curtida(Base):
    __tablename__ = 'curtida'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", backref="Curtida")

    comentario_id = Column(Integer, ForeignKey('comentario.id'))
    comentario = relationship("Comentario", backref="Curtida")

    def __repr__(self):
        return f'Atividade {self.nome}'