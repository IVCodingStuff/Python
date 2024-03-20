nummacas = int(input('Quantas maçãs foram compradas? '))
valor = float()
if nummacas > 12:
    valor = nummacas * 1
else: 
    valor = nummacas * 1.30
print('Valor da maçãs: R${:.2f}'.format(valor))