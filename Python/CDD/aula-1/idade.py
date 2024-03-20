anoatual = 2023
idade = int(input('Qual a sua idade?'))
anonasc = anoatual - idade

if anonasc <= 2005:
    print('Você nasceu em {} e é maior de idade.'.format(anonasc))
else:
    print ('Você nasceu em {} e é menor de idade.'.format(anonasc))