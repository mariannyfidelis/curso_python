"""
# Atributos

* Atributos são representações das características de um determinado _Objeto_ implementado por
uma _Classe_.
* Atributos, na linguagem Python, podem ser subdivididos em:
    * Atributos de Instância
    * Atributos de Classe
    * Atributos Dinâmicos

## Atributos de Instância

São atributos criados dentro do método construtor e fazem referência a instância, ou seja, ao
objeto em questão.

Por exemplo: se criarmos três objetos diferentes, cada objeto poderá possuir atributos de 
instâncias diferentes.

Resumindo: atributos de instâncias fazem referência aos objetos instanciados.
 
"""

class Lampada:
    def __init__(self, voltagem, cor, ligada):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = ligada

class LampadaPriv:
    def __init__(self, voltagem, cor, ligada = False):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = ligada    
    
    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor
    
    @property
    def ligada(self):
        return self.__ligada

