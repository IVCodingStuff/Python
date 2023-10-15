num = int(input('Insira um número de 0 a 20:'))
numeros = ('zero','um', 'dois', 'três', 'quatro','cinco', 'seis', 'sete', 'oito', 'nove','dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'deznove', "vinte")
while True:
    if num >=0 and num <= 20:
        print ('Você digitou o número {}'.format(numeros[num]))
        break
    else:
        num = int(input('Número inválido, tente novamente. Digite um número: '))
        