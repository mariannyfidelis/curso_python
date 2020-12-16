def master():
    def secondary():
        print("Oi")
    return secondary

def master2(funcao):
    def secondary2(*args, **kwargs):
        print("-"*30)
        funcao(*args, **kwargs)
    return secondary2

@master2
def function():
    print("Coisa doida ....")

@master2
def decoradora(texto):
    print(texto)
# Teste 1
func = master()
func()
# Teste 2
teste = master2(function)
teste()
# Teste 3
function()
# Teste 4
decoradora("Coisa complicada ....")