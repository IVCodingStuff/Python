mulheres = int()
maisvelho = int()
nomevelho = str()
media = float()
for c in range (1,2):
    print('----- {}º PESSOA'.format(c))
    nome = (input ('Nome: '))
    idade = int(input ('Idade: '))
    sexo = (input ('Sexo [M/F]: '))
    media += idade
    if idade > maisvelho and sexo == 'M':
        maisvelho = idade
        nomevelho = nome
    if (sexo == 'F') and (idade > 30):
        mulheres = mulheres + 1 
media = media/c
print ('A média de idade do grupo é de {} anos.'.format(media))
print ('O homem mais velho tem {} anos e se chama {}.'.format(maisvelho,nomevelho))
print('Ao todo são {} mulheres com menos de 30 anos.' .format(mulheres))