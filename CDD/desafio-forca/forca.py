from random import randint
from lib import *
palavra = ('carisma', 'inteligencia', 'constituiçao', 'força', 'destreza', 'sabedoria')
numpal = randint(0,5)
palavra_secreta = list(palavra[numpal])
resposta = list('_'*(len(palavra[numpal])))
fim_jogo = False
while fim_jogo == False:
    jogo(palavra_secreta,resposta,tem, n_tem, fim_jogo)
    