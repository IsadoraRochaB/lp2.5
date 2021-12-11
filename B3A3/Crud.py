from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from A3B3.models.models import Cadastro, Cliente, Compra, Editora, Livro


from models.models import Atividade, Comentario, Usuario

engine = create_engine("mysql+pymysql://root:@localhost/B3A3", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create1():
    cliente1 = Cliente(nome='Genis', sobrenome='Rocha Nogueira', codigo='321')

    cadastro1 = Cadastro(endereco='VGA', telefone='8826-6911', cpf='151.891.556.73', lista_de_livros='livro 1')
    cliente1.cadastro.append(cadastro1) 

    compra1 = Compra()
    cliente1.compra.append(compra1)
 
    session.add(cliente1)
    session.commit()
    
def create2():
    cliente2 = Cliente(nome='Rafaela', sobrenome='Rocha Nogueira', codigo='4321')

    cadastro2 = Cadastro(endereco='VGA', telefone='9826-6911', cpf='200.891.556.73', lista_de_livros='livro 2')
    cliente2.cadastro.append(cadastro2) 

    compra2 = Compra()
    cliente2.compra.append(compra2)
 
    session.add(cliente2)
    session.commit()

def create3():
    
    cliente3 = Cliente(nome='Isadora', sobrenome='Rocha Brito', codigo='54321')

    cadastro3 = Cadastro(endereco='VGA', telefone='9826-6911', cpf='300.891.556.73', lista_de_livros='livro 3')
    cliente3.cadastro.append(cadastro3) 

    compra3 = Compra()
    cliente3.compra.append(compra3)
 
    session.add(cliente3)
    session.commit()

def create4():

    editora1 = Editora(nome='LivrosBrito', codigo='321', telefone='7686-6911', gerente='Paulo Henrique')

    livro1 = Livro(titulo='Livro1', autor='Adriela Aparecida', assunto='animais/científico', ISBN='99999-0', quantidade='3')
    editora1.livro.append(livro1) 

    session.add(editora1)
    session.commit()

def create5():

    editora2 = Editora(nome='LivrosBrito', codigo='4321', telefone='3213-6911', gerente='João Carlos')

    livro2 = Livro(titulo='Livro2', autor='Isabela Rocha', assunto='terror/suspense', ISBN='77777-0', quantidade='12')
    editora2.livro.append(livro2) 

    session.add(editora2)
    session.commit()

def create6():

    editora3 = Editora(nome='LivrosBrito', codigo='54321', telefone='3298-6911', gerente='Gabriel Rocha')

    livro3 = Livro(titulo='Livro3', autor='Antonio Augusto', assunto='romance/época', ISBN='99999-0', quantidade='5')
    editora3.livro.append(livro3) 

    session.add(editora3)
    session.commit()