from psutil import users
import psycopg2 as pg
import config
import pandas as pd

#print(config.host, config.user, config.dbname, config.password, config.sslmode)

conn_string = (
    "host={0} user={1} dbname={2} password={3} sslmode={4}"
    .format(config.host, config.user, config.dbname, config.password, config.sslmode)
    )

conexao = 0
try:
    conn = pg.connect(conn_string)
except:
    conexao = 0
    print('Conexão não realizada!')
else:
    conexao = 1
    print('Conexão realizada!')

print(conexao)
    
if conexao == 1:
    cursor = conn.cursor()
    def inserir_bd(nome, idade):
        cursor.execute("INSERT INTO nomepessoa (nome, idade) VALUES (%s, %s);", (nome, idade))
        conn.commit()
        
    def selecionar_bd():
        cursor.execute("SELECT * from nomepessoa;")
        return cursor.fetchall()
        
    #inserir_bd('Dioginys', 20)

    nome_idade = selecionar_bd()

    for i, pessoa in enumerate(nome_idade):
        print('Nome: ', pessoa[0])
        print('Idade: ', pessoa[1])

    print(nome_idade)
    print()

    cursor.close()
    conn.close()