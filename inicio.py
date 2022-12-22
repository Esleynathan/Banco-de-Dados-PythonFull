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
            cursor.execute(f"create table {nomeTabela} (nome varchar(50))")
        print("Tabela criada com sucesso.")
    except Exception as e:
        print (f'Ocorreu um erro {e}')

def removeTabela(nomeTabela):
    try:   
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
        print("Tabela excliuda com sucesso.")
    except Exception as e:
        print (f'Ocorreu um erro {e}') 

def insereTabela(nome):
    try:   
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO teste values ('{nome}')")
        print("Valor inserido com sucesso.")
    except Exception as e:
        print (f'Ocorreu um erro {e}')

def selectTabela(nomeTabela):
    try:   
        with con.cursor() as cursor:
            cursor.execute(f"SELECT * FROM ('{nomeTabela}')")
            resultado = cursor.fetchall()
            print (resultado)
    except Exception as e:
        print (f'Ocorreu um erro {e}')

def updateTabela(nomeAlterar, nomeAlterado):
    try:   
        with con.cursor() as cursor:
            cursor.execute(f"UPDATE teste SET nome = {nomeAlterar} WHERE nome = {nomeAlterado}")
            print('Atualização realizada com sucesso.')
    except Exception as e:
        print (f'Ocorreu um erro {e}')

def deleteTabela():
    try:   
        with con.cursor() as cursor:
            cursor.execute(f"DELETE FROM  teste WHERE nome = 'marco'")
            print('Remoção realizada com sucesso.')
    except Exception as e:
        print (f'Ocorreu um erro {e}')

con.commit()
con.close()