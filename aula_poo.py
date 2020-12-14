class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


if __name__ == "__main__":
    id = 1

    print(type(id))

    c = Produto("caneta", 1)
    print(c)
    print(c.nome)
    print(c.preco)
    print(type(c))
