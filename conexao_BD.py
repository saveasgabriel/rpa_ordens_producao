from psutil import users
import psycopg2 as pg
import config

def realizarConexaoBD():
    
    # Parametros da conexão
    conn_string = (
        "host={0} user={1} dbname={2} password={3} sslmode={4}"
        .format(config.host, config.user, config.dbname, config.password, config.sslmode)
        )
    
    # Tentativa de conexao
    conexao = 0
    try:
        conn = pg.connect(conn_string)
    except:
        conexao = 0
        print('Conexão não realizada!')
    else:
        conexao = 1
        print('Conexão realizada!')
     
    if conexao == 1: 
        return conn
    else:
        return 

conn = realizarConexaoBD()  


def cursor(conn):
    if conn != None:
        cursor = conn.cursor()
        
        def buscarEsacala():
            cursor.execute("SELECT * from escala_abate;")
            return cursor.fetchall()
        
        def inserir_bd(nome, idade):
            cursor.execute("INSERT INTO nomepessoa (nome, idade) VALUES (%s, %s);", (nome, idade))
            conn.commit()
            
        def selecionar_bd():
            cursor.execute("SELECT * from nomepessoa;")
            return cursor.fetchall()
            
        #inserir_bd('Dioginys', 20)

        nome_idade = selecionar_bd()
        abate = buscarEsacala()

        for i, pessoa in enumerate(nome_idade):
            print('Nome: ', pessoa[0])
            print('Idade: ', pessoa[1])
            
        for x, boi in enumerate(abate):
            print('ID: ', boi[0])
            print('Sigla: ', boi[1])

        #print(nome_idade)
        #print(abate)

        cursor.close()
        conn.close()
    else:
        print('SEM CONEXÃO')
        
cursor(conn)