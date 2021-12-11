from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DECIMAL, DateTime

Base = declarative_base()


class Usuario(Base):
    tablename = 'usuario'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(45), nullable=False)


    def repr(self):
        return f'Usuario {self.usuario}'

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()

class Atividade(Base):
    tablename = 'atividade'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    inicio = Column(DateTime(100), unique=True, nullable=False)
    fim = Column(DateTime(100), unique=True, nullable=False)
    quilometros = Column(DECIMAL(10,2), nullable=False)
    tipo = Column(String(100), nullable=False)
    local = Column(String(100), nullable=False)

    def repr(self):
        return f'Atividade {self.atividade}'

class Comentario(Base):
    tablename = 'comentario'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    comentario = Column(String(255), nullable=True)

    def repr(self):
        return f'Comentario {self.comentario}'

class Curtida(Base):
    tablename = 'curtida'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    def repr(self):
        return f'Curtida {self.curtida}'
