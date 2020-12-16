import conta

class Cliente:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


    def __str__(self):
        return f"Cliente: {self.nome}"
