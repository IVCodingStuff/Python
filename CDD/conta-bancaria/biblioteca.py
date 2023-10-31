class Conta:
    def __init__(self, saldo, status):
        self.num = 10
        self.saldo = 500.0
        self.status = True
        self.nome_cliente = 'Mia Calisto'
        self.tipo = 'Conta-corrente'
        self.limite = 1000.0
        self.saldo = saldo
        self.status = status

    def depositar(self,deposito):
        if self.status:
            self.saldo += deposito
            print()
            print('<< Saldo atual: {} >>'.format(self.saldo))
        else:
            print('<< DEPOSITO NEGADO --> CONTA DESATIVADA >>')

    def sacar(self, saque):
        if self.status:
            self.saldo -= saque
            print()
            print('<< Saldo atual: {} >>'.format(self.saldo))
        else:
            print()
            print('SAQUE NEGADO --> CONTA DESATIVADA')

    def verificar_saldo(self):
        if self.status:
            print()
            print('<< Saldo atual: {} >>'.format(self.saldo))
        else:
            print()
            print('<< CONTA DESATIVADA >>')

    def ativar (self):
        if self.status:
            print()
            print ('CONTA JÁ ATIVADA')
        else:
            print()
            print('<< CONTA ATIVADA COM SUCESSO >>')

    def desativar (self):
        if self.status and self.saldo == 0:
            self.status = False
            print()
            print('<< CONTA DESATIVADA COM SUCESSO >>')
        elif self.status and self.saldo > 0:
            print()
            print('<< DESATIVAÇÃO NEGADA\nRETIRE TODO O SALDO DISPONÍVEL E TENTE NOVAMENTE')
        elif self.status == False:
            print('<< CONTA JÁ ESTÁ DESATIVADA >>')

    def parar (self, continuar):
        print()
        print('SISTEMA FINALIZADO')
        continuar = False
        return (continuar)