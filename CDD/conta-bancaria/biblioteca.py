class Conta:
    def __init__(self, saldo, status):
        self.num = 10
        self.nome_cliente = 'Mia Calisto'
        self.tipo = 'Conta-corrente'
        self.limite = 0
        self.saldo = saldo
        self.status = status
        self.status_limite = False

    def depositar(self):
        if self.status == True:
            deposito = float(input('Quanto quer depositar? '))
            self.saldo += deposito
            print('\n<< Saldo atual: {} >>'.format(self.saldo))
            saldo = self.saldo
            return (saldo)
        else:
            print('\n<< DEPOSITO NEGADO --> CONTA DESATIVADA >>')

    def sacar(self):
        if self.status and self.saldo > 0:
            saque = float(input('\nQuanto quer sacar? '))
            self.saldo -= saque
            print('\nSAQUE LIBERADO\n<< Saldo atual: {} >>'.format(self.saldo))
            saldo = self.saldo
            return (saldo)
        elif self.status and self.saldo <= 0:
            print('\nSAQUE NEGADO --> SALDO INDISPONÍVEL')
        elif self.status and saque <= (self.saldo+self.limite):
            if saque > self.saldo:
                resto_saque = self.saldo - saque
                self.saldo -= saque
                self.limite -= resto_saque
                print('SAQUE LIBERADO\n<< Saldo atual: {} >>'.format(self.saldo))
        elif self.status and saque > (self.saldo+self.limite):
            print('\nSAQUE NEGADO --> SALDO INSUFICIENTE')
        else:
            print('\nSAQUE NEGADO --> CONTA DESATIVADA')

    def verificar_saldo(self):
        if self.status == True and self.status_limite == False:
            print('\n<< Saldo atual: {} >>'.format(self.saldo))
            print('Limite: Falso')
        elif self.status and self.status_limite:
            print('\n<< Saldo atual: {} >>'.format(self.saldo+self.limite))
            print('Limite: true')
        else:
            print('\n<< CONTA DESATIVADA >>')

    def ativar (self):
        if self.status:
            print ('\nCONTA JÁ ATIVADA')
            
        else:
            self.status = True
            print('\n<< CONTA ATIVADA COM SUCESSO >>')
            return(self.status)

    def desativar (self):
        if self.status and self.saldo == 0:
            self.status = False
            print('\n<< CONTA DESATIVADA COM SUCESSO >>')
        elif self.status and self.saldo > 0:

            print('\n<< DESATIVAÇÃO NEGADA\nRETIRE TODO O SALDO DISPONÍVEL E TENTE NOVAMENTE')
        elif self.status == False:
            print('\n<< CONTA JÁ ESTÁ DESATIVADA >>')

    def ativar_limite(self):
        self.limite = 1000.0
        self.status_limite = True
        print('SEU LIMITE FOI LIBERADO!\n<< Saldo atual: {} >>'.format(self.saldo+self.limite))

    def parar (self, continuar):
        print('\nSISTEMA FINALIZADO')
        continuar = False
        return (continuar)