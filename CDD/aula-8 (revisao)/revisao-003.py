resp = str()
while resp in 'Ss':
    idade = int(input('Qual a sua idade? '))
    anoAtual = 2023
    anonasc = anoAtual-idade
    mesnasc = int(input('Em que mês você nasceu? '))
    mesAtual = int(input('Em que mês você atual? '))

    if mesAtual >= mesnasc:
        print('Você nasceu em {}'.format(anonasc))
    else:
        print('Você nasceu em {}'.format(anonasc-1))

    if anonasc <= (anoAtual-18):
        print('Você é maior de idade.')
    else:
        print("Você é menor de idade.")
    resp = input('Quer calcular novamente? [S/N]')