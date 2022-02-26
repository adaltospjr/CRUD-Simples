import psycopg2

def consulta():
    host = "localhost"
    dbname = 'postgres'
    user = "postgres"
    password = "123456"

    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cur = conn.cursor()

    cur.execute('select * from cadastro')

    dados = cur.fetchall()
    conn.close()
    cur.close()

    return dados

def gravar(nome, email, senha):
    host = "localhost"
    dbname = 'postgres'
    user = "postgres"
    password = "123456"

    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cur = conn.cursor()

    comando = """ INSERT INTO cadastro (nome, email, senha) VALUES (%s,%s,%s)"""

    insert = (nome, email, senha)

    cur.execute(comando, insert)

    conn.commit()
    conn.close()
    cur.close()

    return 'OK'

gravar('Adalto', 'teste', '1234')
