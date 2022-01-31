
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Artista(Base):
    __tablename__ = 'artista'

    id = Column(Integer, Sequence('artista_id_seq'), primary_key=True)
    nome = Column(String(255), unique=True, nullable=False)
    sobrenome = Column(String(45), nullable=False)

    cadastro_artista = relationship("Cadastro_Artista",backref='Artista', lazy=True)
    musica = relationship("Musica",backref='Artista', lazy=True)

    def __repr__(self):
        return f'Artista {self.artista}'

class Cadastro_Artista(Base):
    __tablename__ = 'cadastro_artista'
    
    id = Column(Integer, Sequence('cadastro_id_seq'), primary_key=True)
    agencia = Column(String(255), unique=True, nullable=False)
    registro = Column(int(255), nullable=False)

    artista_id = Column(Integer, ForeignKey('artista.id'))
    artista = relationship("Artista", backref="Cadastro_Artista")

    def __repr__(self):
        return f'Cadastro_Artista {self.cadastro_artista}'


class Musica(Base):
    __tablename__ = 'musica'

    id = Column(Integer, Sequence('musica_id_seq'), primary_key=True)
    album_ou_ep = Column(String(255), unique=True, nullable=False)
    duracao = Column(String(255), unique=True, nullable=False)
    classificacao = Column(String(255), unique=True, nullable=False)
    
    ouvir = relationship("Ouvir",backref='Musica', lazy=True)

    artista_id = Column(Integer, ForeignKey('artista.id'))
    artista = relationship("Artista", backref="Musica")

    def __repr__(self):
        return f'Musica {self.musica}'


class Ouvinte(Base):
    __tablename__ = 'ouvinte'

    id = Column(Integer, Sequence('ouvinte_id_seq'), primary_key=True)
    nome = Column(String(255), unique=True, nullable=False)
    sobrenome = Column(String(255), unique=True, nullable=False)

    ouvir = relationship("Ouvir",backref='Ouvinte', lazy=True)
    cadastro = relationship("Cadastro",backref='Ouvinte', lazy=True)

    def __repr__(self):
        return f'Ouvinte {self.ouvinte}'

class Cadastro(Base):
    __tablename__ = 'cadastro'
    
    id = Column(Integer, Sequence('cadastro_id_seq'), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)

    ouvinte_id = Column(Integer, ForeignKey('ouvinte.id'))
    ouvinte = relationship("Ouvinte", backref="Cadastro")

    def __repr__(self):
        return f'Cadastro {self.cadastro}'


class Ouvir(Base):
    __tablename__ = 'ouvir'

    id = Column(Integer, Sequence('ouvir_id_seq'), primary_key=True)
    
    musica_id = Column(Integer, ForeignKey('musica.id'))
    musica = relationship("Musica", backref="Ouvir")

    ouvinte_id = Column(Integer, ForeignKey('ouvinte.id'))
    ouvinte = relationship("Ouvinte", backref="Ouvir")

    def __repr__(self):
        return f'Ouvir {self.ouvir}'