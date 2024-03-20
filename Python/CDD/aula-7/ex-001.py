resposta = 'S'
while resposta in 'Ss':
    n1 = int(input('Primeira nota:'))
    while n1 < 0 or n1 > 10:
        print('Nota inválida')
        n1 = int(input ('Primeira nota:'))
    n2 = int(input('Segunda nota:'))
    while n2 < 0 or n2 > 10:
        print('Nota inválida')
        n2 = int(input ('Segunda nota:'))
    media = (n1+n2)/2
    print(media)
    resposta = input('Deseja fazer um novo cálculo?[S/N] ')