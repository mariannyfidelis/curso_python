from random import randint

class Randomica:
    def __init__(self):
        """
        @class
        Metodo construtor da classe Randomica dfgfdgdfgdfg
        """
        self.number = randint(1,3)
        print(f"ola - {self.number}" if self.number==1 else f"oi- {self.number}")

if __name__ == "__main__":
    for i in range(10):
        a = Randomica()
        #print(randint(0,10))