def soma (n1, n2):
    res = n1 + n2
    print('Resposta: {}'.format(res))
    print('')
def sub (n1, n2):
    res = n1 - n2
    print('Resposta: {}'.format(res))
    print('')
def multi (n1, n2):
    res = n1 * n2
    print('Resposta: {}'.format(res))
    print('')
def divi (n1, n2):
    res = n1 / n2
    print('Resposta: {}'.format(res))
    print('')
def piramide (num):
    for c in range(1, num + 1):
        print(str(c) * c, end='\n')
def piramide2 (num):
    for c in range(1, num + 1):
        for d in range(1, num + 1):
            print(x, end='')
            print()
def vogais(frase):
    cont = 0
    for x in frase:
        if x in 'aeiouAEIOU':
            cont += 1
    print('O total de vogais é {}'.format(cont))
def espacos(frase):
    cont = 0
    for x in frase:
        if x in ' ':
            cont += 1
    print('O total de espaços é {}'.format(cont))