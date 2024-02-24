# Valores únicos e em ordem crescente
continuar = True
lista = []
a = 0
while True:
        num = int(input('Digite um número: '))
        while num in lista:
                print('Valor inválido. Tente outro número: ')
                num = int(input('Digite um número: '))
        else:
            lista.append(num)
            print('Valor inserido com sucesso.')
        resposta = input(('Deseja continuar?[S/N] '))
        if resposta in 'Nn':
            break
        a += 1
print('Processo finalizado com sucesso.')
lista.sort()
print('Os números digitados foram {}'.format(lista))
