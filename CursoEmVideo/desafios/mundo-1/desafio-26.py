frase = input("Escreva uma frase: ").upper()
frase = frase.strip()
primeiroa = frase.find('a')
print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('A primeira na posição {}' .format(frase.find('A') + 1))
print('A última na posição {}' .format(frase.rfind('A') + 1))