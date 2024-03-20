repeticao = int(input('Quantas vezes quer repetir? '))
c = 0
valor = int()
media = int()
soma= int()
while c <= repeticao-1:
    valor = int(input('Insira um número:'))
    soma += valor
    c += 1
media = soma/repeticao
print(media)