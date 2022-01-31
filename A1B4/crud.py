from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from models.models import Artista, Cadastro_Artista, Musica, Ouvinte, Cadastro, Ouvir


from models.models import Atividade, Comentario, Usuario

engine = create_engine("mysql+pymysql://root:@localhost/A1B4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create1():
    artista1 = Artista(nome='Taylor', sobrenome='Swift')

    cadastro_artista1 = Cadastro_Artista(agencia='Republic Records', registro='123')
    artista1.cadastro_artista.append(cadastro_artista1) 

    musica1 = Musica(nome='Cardigan', album_ou_ep='folklore', duracao='3 minutos', classificacao='12+')
    artista1.musica.append(musica1) 


    session.add(artista1)
    session.commit()

def create2():
    artista2 = Artista(nome='Shawn', sobrenome='Mendes')

    cadastro_artista2 = Cadastro_Artista(agencia='Island Records', registro='321')
    artista2.cadastro_artista.append(cadastro_artista2) 

    musica2 = Musica(nome='Mercy', album_ou_ep='Illuminate', duracao='2 minutos', classificacao='12+')
    artista2.musica.append(musica2) 


    session.add(artista2)
    session.commit()

def create3():
    artista3 = Artista(nome='Olivia', sobrenome='Rodrigo')

    cadastro_artista3 = Cadastro_Artista(agencia='Geffen Records', registro='213')
    artista3.cadastro_artista.append(cadastro_artista3) 

    musica3 = Musica(nome='Traitor', album_ou_ep='Sour', duracao='4 minutos', classificacao='16+')
    artista3.musica.append(musica3) 


    session.add(artista3)
    session.commit()
    
def create4():

    ouvinte1 = Ouvinte(nome='Igor', Sobrenome='Chaves')

    cadastro1 = Cadastro(email='igor.1904.chaves@gmail.com', senha='789')
    ouvinte1.cadastro.append(cadastro1) 

    ouvir1 = Ouvir()
    ouvinte1.ouvir.append(ouvir1)

    session.add(ouvinte1)
    session.commit()

def create5():

    ouvinte2 = Ouvinte(nome='Isadora', Sobrenome='Rocha')

    cadastro2 = Cadastro(email='isadorarochabrito.rb@gmail.com', senha='987')
    ouvinte2.cadastro.append(cadastro2) 

    ouvir2 = Ouvir()
    ouvinte2.ouvir.append(ouvir2)

    session.add(ouvinte2)
    session.commit()

def create6():

    ouvinte3 = Ouvinte(nome='Sabrina', Sobrenome='Sousa')

    cadastro3 = Cadastro(email='sabrinasousalaves@gmail.com', senha='978')
    ouvinte3.cadastro.append(cadastro3) 

    ouvir3 = Ouvir()
    ouvinte3.ouvir.append(ouvir3)

    session.add(ouvinte3)
    session.commit()





