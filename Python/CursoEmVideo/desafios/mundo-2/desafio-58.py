import random
ia = random.randint(0,10)
print('Tente advinhar o número que estou pensando. É um de 0 a 10.')
player = int(input('Dê um palpite: '))
palpites = 1
while player != ia:
    print('Errrrrrrrrrou. Tenta de novo')
    player = int(input('Dê mais um palpite: '))
    palpites = palpites + 1
print('Boa! Eu pensei {}. Acertou depois de {} palpites'.format(ia, palpites))
