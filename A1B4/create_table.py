from sqlalchemy import *
from models.models import Artista, Cadastro_Artista, Musica, Ouvinte, Cadastro, Ouvir


engine = create_engine("mysql+pymysql://root:@localhost/A1B4", echo=True)

artista = Artista.__table__
artista.create(engine, checkfirst=True)

cadastro_artista = Cadastro_Artista.__table__
cadastro_artista.create(engine, checkfirst=True)

musica = Musica.__table__
musica.create(engine, checkfirst=True)

ouvinte = Ouvinte.__table__
ouvinte.create(engine, checkfirst=True)

cadastro = Cadastro.__table__
cadastro.create(engine, checkfirst=True)

ouvir = Ouvir.__table__
ouvir.create(engine, checkfirst=True)


