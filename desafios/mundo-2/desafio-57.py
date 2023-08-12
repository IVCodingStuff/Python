sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Valor inválido.')
    sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()[0]
print ('Sexo {} armazenado com sucesso'.format(sexo))