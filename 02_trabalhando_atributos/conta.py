def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def extrato(conta):
    print("{} possui {} reais na conta".format(conta["titular"], conta["saldo"]))

def saca(conta, valor):
    conta["saldo"] -= valor

def deposita(conta, valor):
    conta["saldo"] += valor


if __name__ == "__main__":
    c1 = cria_conta(1,"JJ", 1000, 100)
    c2 = cria_conta(2,"AA", 500, 500)

    saca(c1, 500)
    extrato(c1)
    deposita(c1, 1500)
    extrato(c1)
