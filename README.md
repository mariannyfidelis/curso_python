# Linguagem Python

## O que é Python ?

- Criada em 1991
- Linguagem multiparadigma
- Linguagem de alto nível de propósito geral
- Utilizada na Web, Estatística, Ciência de dados, entre outras aplicações;

> **import this**  
> Você verá que o _Zen of Python_ será apresentado a você  
> Easter eggs segredos sobre um artefato !!!  

## Ambiente Virtual Python

Quando desenvolvemos com Python "globalmente", ou seja, diretamente com o Python instaldo no SO, em vez de isolarmos os ambientes de cada projeto em desenvolvimento, podemos ter conflitos entre versões de bibliotecas.

Vamos criar um exemplo hipotético: imagine que estamos a desenvolver um projeto onde determinada biblioteca "colorama" só seja possível usar com o Python 3.7 e em outro projeto queremos fazer uso de um biblioteca chamada "numpy" utilizando os últimos recursos do Python 3.8.

Se não criarmos **ambientes virtuais** isso não será possível !

1. Duas bibliotecas interessantes: 'virtualenv e virtualenvwrapper-win'
2. Estas ferramentas são muito poderosas e nos permite criar ambientes isolados de desenvolvimento Python. 
3. Ou seja, torna possível a utilização de diversas bibliotecas em um mesmo ambiente sem que haja conflito entre elas. 
4. Você isola ambientes do Sistema Operacional e de outros projetos.

### Como funciona um ambiente virtual

O funcionamento é bastante simples, ele basicamente cria uma cópia de todos os diretórios necessários para que um programa Python seja executado.

Desta forma, ao instalar uma nova biblioteca será **colocada no diretório do virtualenv** e não mais de forma global no sistema operacional.

![](https://debugeverything.com/wp-content/uploads/2020/04/python-virtualenv.001-1.jpeg)


Desta forma, um programador profissional Python irá criar para cada projeto um ambiente virtual, de preferência com o mesmo nome do projeto para que seja fácil encontrar e fazer uso. 

Exemplo: imagine que temos que implementar um projeto **ecommerce**. Então devemos criar um ambiente virtual de nome _ecommerce_ da seguinte maneira no terminal _**mkvirtualenv ecommerce**_.

Ao usar a IDE PyCharm, ao criar um novo projeto, podemos criar um novo ambiente virtual automaticamente com o mesmo nome do projeto.

### Criando um ambiente virtual

* pip --version
* pip install --upgrade pip
* pip install virtualenv virtualenvwrapper-win

* Criar variável de ambiente 'WORKON_HOME' e colocar diretório 'C:\Users\username\Envs'

* mkvirtualenv nome_ambiente

## Antes de iniciar vamos entender algumas coisas importantes

### DIR e HELP no Python

* DIR - apresenta todos os atributos e funções/métodos disponíveis para determinado tipo ou variável.
* HELP - Apresenta a documentação sobre como utilizar os atributos/propriedades e funções/métodos disponíveis para determinado tipo de dado ou variável.
 
Para usar o **dir** faça: **dir(tipo de dado/variável)**
_____

**Vamos praticar**

```bash
dir("Programação OO")
help("POO".lower)
```

Observe que acima no **dir** ele fornece atributos e métodos sobre o tipo String e o **help** uma descrição sobre o método/fução lower.
_____


## O que é algoritmo ?

- Sequência de passos lógicos e bem definidos para a resolução de um problema
- Podeser computacional ou não computacional

## Entrada de dados no Python

A seguir exemplos de entradas de dados no python desde a versão 2.x até a atual 3.x

```bash
print("Nome:")
nome = input()
idade = input("Idade:")
print("Seja bem-vindo %s" %(nome))
print("Seja bem-vindo {0}".format(nome))
print(f"Seja bem vindo {nome}")
print(f"{nome} tem {int(idade)} anos")
print(f"{nome} nasceu em {2020 - int(idade)}")
```
 
## Tipos de dados

### Números

### Strings


### Listas

### Tuplas

### Dicionários

