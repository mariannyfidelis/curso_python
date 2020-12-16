from cliente import Cliente

class Conta:

    tipo_conta = "Corrente"

    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def __str__(self):
        return f'Conta:[{self.cliente}]\nSaldo:[{self.saldo}]\nTipo:[{self.tipo_conta}]'

    def transfere(self, valor, outraConta):
        self.saldo -= valor
        outraConta.saldo += valor


if __name__ == '__main__':
    c1 = Conta("JJ", 1000.0)
    c2 = Conta("Maria", 2000.0)
    print(c1,c1.tipo_conta)
    print(c2, c2.tipo_conta)
    Conta.tipo_conta = "Poupança"
    print(c1, c1.tipo_conta)
    print(c2, c2.tipo_conta)
    c1.tipo_conta = "ddfggdfg"
    print(c1, c1.tipo_conta)
    print(c2, c2.tipo_conta)