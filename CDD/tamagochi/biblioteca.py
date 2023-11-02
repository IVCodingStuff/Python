class Tamagochi:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self, comida):
       
       self.comendo = True
       if self.comendo == True:
        print('Isa já está comendo {}'.format(comida))
       else:
          print('{} está comendo {}.'.format(self.nome, comida))
    def falar(self):
        print('{} está falando'.format(self.falando))
        self.comendo = True
       
    def dormir(self):
        print('{} está dormindo'.format(self.dormindo))
        self.comendo = True
    
    def acordou(self):
        print('{} acordou.'.format(self.nome))