from sqlalchemy import *
from models.models import Cliente, Cadastro, Compra, Editora, Livro


engine = create_engine("mysql+pymysql://root:@localhost/B3A3", echo=True)

cliente = Cliente.__table__
cliente.create(engine, checkfirst=True)

cadastro = Cadastro.__table__
cadastro.create(engine, checkfirst=True)

editora = Editora.__table__
editora.create(engine, checkfirst=True)

livro = Livro.__table__
livro.create(engine, checkfirst=True)

compra = Compra.__table__
compra.create(engine, checkfirst=True)
