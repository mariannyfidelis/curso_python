# Exemplos de funções com parâmetros **OBRIGATÓRIOS**
def full_name(nome, sobrenome):
    print(f"{nome} {sobrenome}")
    return f"{nome} {sobrenome}"

def expoente(numero, potencia):
    return numero**potencia 

# Vamos refatorar a função _EXPOENTE_anterior para os parâmetros serem opcionais

def expoente2(numero, potencia=2):
    return numero**potencia

print(expoente(2,3))
print(expoente2(2))
print(expoente2(2,3))

# Utilizando argumentos nomeados e parâmetros obrigatórios
full_name(nome="Marianny", sobrenome="Mariano")
full_name(sobrenome="Mariano", nome="Marianny")

