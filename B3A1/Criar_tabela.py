from sqlalchemy import *

from models.models import Usuario, Atividade, Comentario, Curtida

engine = create_engine("mysql+pymysql://root:@localhost/B3A1", echo=True)

usuario = Usuario.table
usuario.create(engine, checkfirst=True)

atividade = Atividade.table
atividade.create(engine, checkfirst=True)

comentario = Comentario.table
comentario.create(engine, checkfirst=True)

curtida = Curtida.table
curtida.create(engine, checkfirst=True)