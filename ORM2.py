from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

x = Pessoa(nome = 'Marcos', usuario ='userMarcos', senha ='12')
y = Pessoa(nome = 'Paulo', usuario ='userPaulo', senha ='00')

session.add_all([x,y])
session.commit()