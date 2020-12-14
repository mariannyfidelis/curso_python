def seja_educado(funcao):
    def sendo_educado():
        print("Olá é um prazer conhecer você !")
        funcao()
        print("Até mais ! E tenha um ótimo dia !")
    return sendo_educado

def saudacao():
    print("Seja bem vindo(a) a nossa instituição !")

# Testando a nossa função simples
print("*"*40)
saudacao()
print("*"*40)

# Testando a nossa função decorada
t = seja_educado(saudacao)
t()
print("*"*40)
