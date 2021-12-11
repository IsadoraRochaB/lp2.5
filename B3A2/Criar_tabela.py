from sqlalchemy import *

from models.models import Usuario, Atividade, Comentario, Curtida

engine = create_engine("mysql+pymysql://root:@localhost/B3A2", echo=True)

usuario = Usuario.__table__
usuario.create(engine, checkfirst=True)

atividade = Atividade.__table__
atividade.create(engine, checkfirst=True)

comentario = Comentario.__table__
comentario.create(engine, checkfirst=True)

curtida = Curtida.__table__
curtida.create(engine, checkfirst=True)