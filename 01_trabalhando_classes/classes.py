"""
- Classes são abstrações que nos permitem modelar objetos do mundo real computacionalmente.
- Imagine que queremos modelar uma lâmpada de nossa casa:
    - Classe Lâmpada deverá ter:
        - Atributos      --> (voltagem 110/220, luminosidade, cor)
        - Comportamentos --> (ligar/desligar)
"""

"""
* Em python para definir uma classe utilizamos a palavra reservada **class**
* Utilizamos a palavra **pass** para identificar um blobo de código ainda não implementado
* **Importante**
   * Não utilizamos _acentuação_, _caracteres especiais_, _espaços_ ou _similares_ para nomear 
   Classe, atributos, arquivos, diretórios e etc.
"""

class Lampada:
    pass

class ContaCorrente:
    pass

class Produto:
    pass

class Contato:
    pass

print("-"*20)
lamp = Lampada()
print(lamp)
print(type(lamp))
print("-"*20)

"""
cc = ContaCorrente()
print(cc)
print(type(cc))
print("-"*20)

produto = Produto()
print(produto)
print(type(produto))
print("-"*20)

contato = Contato()
print(contato)
print(type(contato))
print("-"*20)
"""
print(help(int))