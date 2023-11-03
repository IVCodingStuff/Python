class Tamagotchi:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self):
        if self.dormindo:
            print('{} não pode comer pois está dormindo.'.format(self.nome))
        elif self.falando:
            print('{} não pode comer pois está falando.'.format(self.nome))
        else:
            self.comendo = True
            print('{} foi comer.'.format(self.nome))

    def falar(self):
        if self.comendo:
            print('{} não pode falar pois está comendo.'.format(self.nome))
        elif self.dormindo:
            print('{} não pode falar pois está dormindo.'.format(self.nome))
        else:
            self.falando = True
            print('{} está falando.'.format(self.nome))

    def dormir(self):
        if self.comendo:
            print('{} não pode dormir pois está comendo.'.format(self.nome))
        elif self.falando:
            print('{} não pode dormir pois está falando.'.format(self.nome))
        else:
            self.dormindo = True
            print('{} foi dormir.'.format(self.nome))
    
    def acordou(self):
        if self.dormindo:
            self.dormindo = False
            print('{} acordou.'.format(self.nome))
        else:
            print('{} Não está dormindo.'.format(self.nome))

    def falou(self):
        if self.falando:
            self.falando = False
            print('{} parou de falar.'.format(self.nome))
        else:
            print('{} Não está falando.'.format(self.nome))
    
    def comeu(self):
        if self.comendo:
            self.comendo = False
            print('{} terminou de comer.'.format(self.nome))
        else:
            print('{} Não está comendo.'.format(self.nome))

    def parar (self, continuar):
        print('\nTchauzinho!')
        continuar = False
        return (continuar)
    