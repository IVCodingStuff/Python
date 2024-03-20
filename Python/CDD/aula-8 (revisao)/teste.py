idade = int(input('Qual a sua idade? '))
anoAtual = 2023
anonasc = anoAtual-idade
mesnasc = int(input('Em que mês você nasceu? '))
mesAtual = int(input('Em que mês você atual? '))

if mesAtual >= mesnasc:
    print(anonasc)
else:
    print(anonasc-1)

