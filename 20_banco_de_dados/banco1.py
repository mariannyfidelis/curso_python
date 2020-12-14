import sqlite3


# CRIAR A CONEXÃO
def cria_conexao(banco="basededados1.db"):
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()
    return cursor, conexao
# CRIAR A TABELA COM COMANDO SQL


def cria_tabela(cursor):
    cursor = cursor
    cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   'nome TEXT,'
                   'peso REAL'
                   ')')
# INSERINDO DADOS NA TABELA


def inserir_dado(cursor, conexao, nome, peso):
    cursor.execute('INSERT INTO clientes(nome, peso) VALUES ("Edson", "22")')
    conexao.commit()


def inserir_dado_2(cursor, conexao, nome, peso):
    cursor.execute(
        'INSERT INTO clientes(nome, peso) VALUES (?, ?)', (nome, peso))
    conexao.commit()


def inserir_dado_3(cursor, conexao, nome, peso):
    cursor.execute('INSERT INTO clientes VALUES (:id,:nome,:peso)',
                   {"id": None, "nome": "Lucy", "peso": 45})
    conexao.commit()
# BUSCANDO/SELECIONANDO VALORES NA TABELA


def seleciona(cursor):
    print("*"*25)
    cursor.execute('SELECT * FROM clientes')
    print(cursor)
    for linha in cursor.fetchall():
        print("*"*25)
        print(linha)
    print("*"*25)


def seleciona_2(cursor):
    cursor.execute('SELECT * FROM clientes')
    # desempacotar ...
    for linha in cursor.fetchall():
        id, nome, peso = linha
        print(f'ID:[{id}]\nNome: [{nome}]\nPeso:[{peso}]')


def seleciona_peso(cursor, peso):
    cursor.execute('SELECT nome, peso FROM clientes WHERE peso>:peso',
                   {"peso": peso}
                   )
    # desempacotar ...
    for linha in cursor.fetchall():
        nome, peso = linha
        print(f'Nome: [{nome}]\nPeso:[{peso}]')


# ATUALIZANDO /UPDATE NA TABELA
def update(cursor):
    cursor.execute(
        'UPDATE clientes SET  nome=:nome,id=:id WHERE id=:id',
        {"nome": "Francisco", "id": 2}
    )


def update_2(cursor, n):
    cursor.execute(
        f'UPDATE clientes SET  nome=:nome WHERE id=:id',
        {"nome": n, "id": 3}
    )


def update_3(cursor, n, p):
    cursor.execute(
        f'UPDATE clientes SET  nome=:nome, peso=:peso WHERE id=:id',
        {"nome": n, "peso": p, "id": 3}
    )


# DELETANDO/EXCLUINDO DADOS NA TABELA
def delete_por_identificador(cursor, identificador):
    cursor.execute('DELETE FROM clientes WHERE id=:id',
                   {"id": identificador})


def delete_por_nome(cursor, name):
    cursor.execute('DELETE FROM clientes WHERE nome=:nome',
                   {"nome": name})


if __name__ == "__main__":
    b = "banco_criado_com_dbBrowser.db"
    cursor, conexao = cria_conexao(b)
    cria_tabela(cursor)
    inserir_dado(cursor, conexao, "Marianny", "68")
    inserir_dado_2(cursor, conexao, "JJ", "76")
    inserir_dado_3(cursor, conexao, "Assis", "66")
    print("**"*25)
    seleciona(cursor)
    print("=="*25)
    seleciona_2(cursor)
    print("=="*25)
    print("**"*25)
    update_3(cursor, "José", 98)
    print("!!"*25)
    seleciona_2(cursor)
    print("!!"*25)
    print("..........  DELETANDO .........")

    delete_por_identificador(cursor, 2)
    delete_por_nome(cursor, "Marianny")

    print("..........  SELECIONANDO .........")
    seleciona_2(cursor)
    print("..........  SELECIONANDO POR PESO .........")
    seleciona_peso(cursor, 75)
    cursor.close()
    conexao.close()
