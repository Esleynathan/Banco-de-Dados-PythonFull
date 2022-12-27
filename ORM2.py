from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from ORM import Pessoa


def RetornaSession():

    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "aulapythonfull"
    PORT = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine (CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = RetornaSession()

## AULA SELECT ##
# # x = session.query(Pessoa).all()
# x = session.query(Pessoa).filter(Pessoa.nome == 'marcos').filter(Pessoa.usuario == 'userMarcos')
# x = session.query(Pessoa).filter_by(nome='Marcos', usuario='userMarcos')
# for i in x:
#     print (i.id)
# print(x)
## ## ## ## ## ##

## AULA OPERADOR OR ##
# x = session.query(Pessoa).filter(or_(Pessoa.nome == 'esley', Pessoa.usuario == 'userEsley')).all()
# for i in x:
#     print (i.id)    
## ## ## ## ## ##

## AULA UPDATE ##
# x = session.query(Pessoa).filter(Pessoa.id == '2').all()
# x[0].nome = 'Adailza'
# x[0].usuario = "userAdailza"
# x[0].senha = '140369'
# print(x[0].id)
#   
## ## ## ## ## ##

## AULA DELETE ##
#x = session.query(Pessoa).filter(Pessoa.id == '2').delete()
x = session.query(Pessoa).filter(Pessoa.id == 3).one()
print(x)
# session.delete(x[0])
session.commit() 
## ## ## ## ## ##