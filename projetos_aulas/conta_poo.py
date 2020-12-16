class Conta:
    def __init__(self, nome = "JJ", saldo = 0.0):
        self.nome = nome
        self.__saldo = saldo

    def __add__(self, other):
        saldo_final = self.__saldo + other.__saldo
        return Conta(nome="A definir", saldo=saldo_final)

    def __str__(self):
        return f"""Conta:
    Titular:{self.nome}
    Saldo:{self.__saldo} 
    """


if __name__ == '__main__':
    print("Arquivo conta_poo.py")
    c = Conta(saldo=100)
    print(c, end="")
    print()
    cc = Conta("Marianny", 2000.0)
    print(cc, end="")
    d = c + cc
    print()
    print(d)
    e = d
    print(id(d))
    print(id(e))
