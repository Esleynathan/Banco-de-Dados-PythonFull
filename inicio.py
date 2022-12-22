import pymysql.cursors


con = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    port = 3306,
    db="aulapythonfull",
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)

def criaTabela(nomeTabela):
    try:   
        with con.cursor() as cursor:
            cursor.execute("create table teste (nome varchar(50))")
        print("Tabela criada com sucesso.")
    except Exception as e:
        print (f'Ocorreu um erro {e}')

def removerTabela(nomeTabela):
    try:   
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
        print("Tabela excliuda com sucesso.")
    except Exception as e:
        print (f'Ocorreu um erro {e}')        
criaTabela('Teste2')
