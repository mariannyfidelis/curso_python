def soma(number1, number2):
    return number1+number2

def subtracao(number1, number2):
    if number1 >= number2:
        return number1 - number2
    return number2 - number1

def operacao(number1, number2, funcao = soma):
    return funcao(number1, number2)

print(soma(1,2))
print(subtracao(1,2))

print(operacao(2,3))

print(operacao(2,3, soma))

print(operacao(2,3, subtracao))

# Explicação e exemplo sobre a diferença entre variáveis locais e globais

"""
# Variáveis locais

def funcao():
    professor = "João da Silva"
    return f"Olá professor(a) {professor} !!!"

print(funcao())
# Tentando usar uma variável local fora de seu escopo
print(professor)

"""

"""
# Variáveis globais

total = 0

def incrementa_total():
    global total # Informando que queremos utilizar a variável global
    total += 1
    return total

# Usando a variável global

print(incrementa_total())
"""

"""
# Exemplo de funções que são declaradas internamente em outras funções e possuem variáveis com um escopo especial

def funcao_externa():
    contador = 0

    def funcao_interna():
        nonlocal contador
        contador += 2
        return contador
    return funcao_interna()

# Exemplo de uso da função externa

print(funcao_externa())
print(funcao_externa())
print(funcao_externa())

# A função interna não é reconhecida

print(funcao_interna()) # Causará um erro !!!

"""