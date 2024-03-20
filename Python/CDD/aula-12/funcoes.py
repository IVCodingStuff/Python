def estoque(quant,preco,nome):
    valEstoque = quant*preco
    return valEstoque, nome
def pnz (num):
    if num == 0:
        return ("Z")
    if num < 0:
        return ("N")
    if num > 0:
        return ("P")
def adicao (*num):
    soma = 0
    for c in num:
        soma += c
    return soma
def letras(frase):
    cont = 0
    for x in frase:
        if x not in ' ':
            cont += 1
    print('O total de letras é {}'.format(cont))
    for i  in range (len(frase)-1, -1,-1):
        print(frase[i], end="")
