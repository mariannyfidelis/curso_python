import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
    
    def inserir(self, nome, telefone):
        consulta = "INSERT or IGNORE INTO agenda (nome, telefone) VALUES (?,?)"
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = "UPDATE or IGNORE agenda SET nome=?, telefone = ? WHERE id=?"
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self):
        consulta = "DELETE FROM agenda WHERE id=?"
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM AGENDA")
        self.conn.commit()

        for linha in self.cursor.fetchall():
            print(linha)
    
    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    agenda = AgendaDB("./20_banco_de_dados/db_agenda/agenda.db")
    agenda.inserir("Ana", "111111")
    agenda.listar()