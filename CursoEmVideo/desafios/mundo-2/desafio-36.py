valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
tempo = int(input('Em quantos anos você vai pagar? '))
prestacao = tempo*12
valprestacao = valor/(tempo*12)
orcamento = (sal*30)/100

if prestacao <= orcamento:
    print ('Você pode financiar a casa. Terá que pagar {} prestações de R${:.2f} durante {} anos.'.format(prestacao, valprestacao, tempo))
else:
    print ('Infelizmente, você não pode financiar a casa.')