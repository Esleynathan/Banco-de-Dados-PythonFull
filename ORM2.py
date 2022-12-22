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

x = session.query(Pessoa).all()

# x = session.query(Pessoa).filter(Pessoa.nome == 'marcos').filter(Pessoa.usuario == 'userMarcos')
x = session.query(Pessoa).filter_by(nome='Marcos', usuario='userMarcos')

for i in x:
    print (i.id)

print(x)