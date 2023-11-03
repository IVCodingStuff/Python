class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print('{} foi comer.'. format(self.nome))
    def barulho(self):
        print('{} está fazendo barulho'.format(self.nome))

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f"{self.nome} está miando...")


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        self.nome = nome
        self.cor = cor

    def emitirSom(self):
        print(f"{self.nome} está latindo...")


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        self.nome = nome
        self.cor = cor

    def emitirSom(self):
        print(f"{self.nome} está chiando...")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        self.nome = nome
        self.cor = cor

    def emitirSom(self):
        print(f"{self.nome} está fazendo mugindo...")