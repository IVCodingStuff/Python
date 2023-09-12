nota1 = int(input('Insira sua primeira nota: '))
nota2 = int(input('Insira sua segunda nota: '))
media = (nota1 + nota2)/2

if media >= 6: 
    print('Parabéns você foi aprovado com {} de média!'.format(media))
else:
    print ('Infelizmente você foi reprovado com {} de média. Tente mais da próxima vez!'.format(media))
