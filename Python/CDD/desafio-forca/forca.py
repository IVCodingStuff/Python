from random import randint
from lib import *
palavra = ('carisma', 'inteligencia', 'constituiçao', 'força', 'destreza', 'sabedoria')
numpal = randint(0,5)
palavra_secreta = list(palavra[numpal])
resposta = list('_'*(len(palavra[numpal])))
n_tem = 1
tem = 0
fim_jogo = 0
letras_digitadas = []
while fim_jogo == 0:
    resultados = jogo(palavra_secreta,resposta,tem, n_tem, fim_jogo, letras_digitadas)
    n_tem = resultados[0]
    fim_jogo = resultados[1]
    letras_digitadas = resultados[2]