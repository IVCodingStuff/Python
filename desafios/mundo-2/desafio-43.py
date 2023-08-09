peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso/altura**2

if imc < 18.5:
    print('Status: ABAIXO DO PESO')

elif imc >= 18.5 and imc < 25:
    print('Status: PESO IDEAL')

elif imc >= 25 and imc < 30:
    print('Status: SOBREPESO')

elif imc >= 35 and imc <= 40:
    print('Status: OBESIDADE')

elif imc > 40:
    print('Status: OBESIDADE MÓRBIDA')
