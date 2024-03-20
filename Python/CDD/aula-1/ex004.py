nome = input('Insira o seu nome: ')
idade = int(input('Insira a sua idade: '))
sal = float(input('Insira o seu salário: '))
pcaumento = float(input('Qual a porcentagem do aumento? '))
filhos = int(input('Quantos filhos você tem? '))
abono = float (filhos*150)
aumento = sal + (sal*pcaumento)/100 + abono
ferias = (sal + (sal*pcaumento)/100)/3
total = aumento + ferias
print('Nome: {}\nIdade: {}\nSalário: {}\nAumento (com abono): {}\nFérias (sem abono): {}\nTotal: {}'.format(nome, idade, sal, aumento,ferias,total))
