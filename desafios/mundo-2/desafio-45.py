import random
jokenpo = random.randint(1,3)

print('====== JOKENPO ======')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
jogador = int(input('O que você vai jogar? '))

if jokenpo  == 1:
    ia = 'Pedra'
elif jokenpo  == 2:
    ia = 'Papel'
elif jokenpo  == 3:
    ia = 'Tesoura'
    
if jogador  == 1:
    player = 'Pedra'
elif jogador  == 2:
    player = 'Papel'
elif jogador  == 3:
    player = 'Tesoura'

if player == ia:
    print ('{} X {}'.format(player, ia))
    print ('EMPATE')
elif (player == "Pedra"):
    if (ia == 'Tesoura'):
        print ('{} X {}'.format(player, ia))
        print ('VOCÊ VENCEU')
    elif (ia == 'Papel'):
        print ('{} X {}'.format(player, ia))
        print ('VOCÊ PERDEU')

elif (player == 'Papel'):
    if (ia == 'Pedra'):
        print ('{} X {}'.format(player, ia))
        print ('VOCÊ VENCEU')
    elif (ia == 'Tesoura'):
        print ('{} X {}'.format(player, ia))
        print ('VOCÊ PERDEU')

elif (player == 'Tesoura'):
    if (ia == 'Papel'):
        print ('{} X {}'.format(player, ia))
        print ('VOCÊ VENCEU')
    elif (ia == 'Pedra'):
        print ('{} X {}'.format(player, ia))
        print ('VOCÊ PERDEU')