from funcoes import estoque
nome = input("Nome do Produto: ")
quant = int(input('Quantidade: '))
preco = float(input('Preço: '))
valEstoque = estoque (quant, preco, nome)
nome_produto = estoque(quant, preco, nome)
print('Valor de {} no estoque: {}'.format(valEstoque[1], valEstoque[0]))