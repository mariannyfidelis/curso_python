from random import choice

def cumprimentar_pessoa(pessoa):
    def humor_do_dia():
        return choice(['E aí, bele ? ', 'Não estou a fim de conversar ! ', 'Gosto muito de você ! '])
    return humor_do_dia()+ pessoa 

print(cumprimentar_pessoa("Maria"))