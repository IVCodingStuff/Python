import os
def jogo(palavra_secreta,resposta,tem, n_tem, fim_jogo, letras_digitadas):
    while True:
        letra = input('Qual letra quer tentar? ').lower()
        letras_digitadas.append(letra)
        print()
        for a in range(len(resposta)):
            if letra in palavra_secreta[a]:
                resposta[a] = letra
                tem = 1
        if tem == 0:
            n_tem += 1
        os.system('cls')  
        print('Letras digitadas: {}'.format(letras_digitadas))
        print()
        print(resposta)
        print()
        
        tem = 0
        if resposta == palavra_secreta:
            print('VOCÊ VENCEU!')
            fim_jogo = True
            break
        elif n_tem == 1:
            print ('____\n|   |\n|\n|\n|\n|')
        elif n_tem == 2:
            print ('____\n|   |\n| (>o<)\n|\n|\n|')
        elif n_tem == 3:
            print ('____\n|   |\n| (>o<)\n|   | \n|   \n|')
        elif n_tem == 4:
            print ('____\n|   |\n| (>o<)\n|  /| \n|   \n|')
        elif n_tem == 5:
            print ('____\n|   |\n| (>o<)\n|  /|\ \n|   \n|')
        elif n_tem == 6:
            print ('____\n|   |\n| (>o<)\n|  /|\ \n|   |\n| _/')
        elif n_tem == 7:
            print ('____\n|   |\n| (xox)\n|  /|\ \n|   |\n| _/_\_')
            print('VOCÊ PERDEU!')
            fim_jogo = 1
            break
          
    return [n_tem, fim_jogo, letras_digitadas]