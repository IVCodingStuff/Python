from random import randint
palavra = ('carisma', 'inteligencia', 'constituiçao', 'força', 'destreza', 'sabedoria')
numpal = randint(0,5)
palavra_secreta = list(palavra[numpal])
resposta = list('_'*(len(palavra[numpal])))
n_tem = 0
tem = 0
print(palavra[numpal])
while True:
    tem = 0
    letra = input('Qual letra quer tentar? ')
    for a in range(len(resposta)):
        if letra in palavra_secreta[a]:
            resposta[a] = letra
            tem = 1
    if tem == 0:
        n_tem += 1
    print(resposta)
    if resposta == palavra_secreta:
        print('VOCÊ VENCEU!')
        break
    elif n_tem == 0:
        print ('____\n|   |\n|\n|\n|\n|')
    elif n_tem == 1:
        print ('____\n|   |\n| (>o<)\n|\n|\n|')
    elif n_tem == 2:
        print ('____\n|   |\n| (>o<)\n|   | \n|   \n|')
    elif n_tem == 3:
        print ('____\n|   |\n| (>o<)\n|  /| \n|   \n|')
    elif n_tem == 4:
        print ('____\n|   |\n| (>o<)\n|  /|\ \n|   \n|')
    elif n_tem == 5:
        print ('____\n|   |\n| (>o<)\n|  /|\ \n|   |\n| _/')
    elif n_tem == 6:
        print ('____\n|   |\n| (xox)\n|  /|\ \n|   |\n| _/_\_')
        print('VOCÊ PERDEU!')
        break