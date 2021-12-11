from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker


from models.models import Atividade, Comentario, Usuario

engine = create_engine("mysql+pymysql://root:@localhost/B3A2", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create1():
    user1 = Usuario(email='usu1@usu.com', senha='123')

    atividade1 = Atividade(inicio='27-11-2021', fim='27-11-2021', quilometro='10,5', tipo='corrida', local='VGA')
    user1.atividade.append(atividade1) 

    atividade2 = Atividade(inicio='28-11-2021', fim='28-11-2021', quilometro='22,00', tipo='corrida', local='VGA')
    user1.atividade.append(atividade2)

    atividade3 = Atividade(inicio='29-11-2021', fim='29-11-2021', quilometro='30,00', tipo='corrida', local='VGA')
    user1.atividade.append(atividade3)

    comentario1 = Comentario(comentario='exautivo...porém revigorante')
    user1.comentario.append(comentario1)
    
    session.add(user1)
    session.commit()
    
def create2():
    user2 = Usuario(email='usu2@usu.com', senha='123')

    atividade4 = Atividade(inicio='27-11-2021', fim='27-11-2021', quilometro='10,5', tipo='corrida', local='VGA')
    user1.atividade.append(atividade1) 

    atividade5 = Atividade(inicio='28-11-2021', fim='28-11-2021', quilometro='22,00', tipo='corrida', local='VGA')
    user1.atividade.append(atividade2)

    atividade6 = Atividade(inicio='29-11-2021', fim='29-11-2021', quilometro='30,00', tipo='corrida', local='VGA')
    user1.atividade.append(atividade3)


    comentario2 = Comentario(comentario='Eletrizante!')
    user2.comentario.append(comentario2)

    comentario3 = Comentario(comentario='A melhor coisa que fiz em toda minha vida!')
    user2.comentario.append(comentario3)

    session.add(user2)
    session.commit()

def create3():
    user3 = Usuario(email='usu3@usu.com', senha='123')

   atividade7 = Atividade(inicio='27-11-2021', fim='27-11-2021', quilometro='10,5', tipo='corrida', local='VGA')
    user1.atividade.append(atividade1) 

    atividade8 = Atividade(inicio='28-11-2021', fim='28-11-2021', quilometro='22,00', tipo='corrida', local='VGA')
    user1.atividade.append(atividade2)

    atividade9 = Atividade(inicio='29-11-2021', fim='29-11-2021', quilometro='30,00', tipo='corrida', local='VGA')
    user1.atividade.append(atividade3)


    comentario4 = Comentario(comentario='Odiei cada segundo')
    user3.comentario.append(comentario4)

    session.add(user3)
    session.commit()

def update():

    user = session.query(Usuario).filter(Usuario.id == 1).one()
    user.senha = "senhausu1"
    session.commit()

def delete():

    atividade = session.query(Atividade).get(2)
    session.delete(atividade)
    session.commit()