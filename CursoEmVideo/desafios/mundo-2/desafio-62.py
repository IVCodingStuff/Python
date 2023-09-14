soma = int()
termosmais = int()
primeirotermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
c = 1
while c <= 10:
    soma = (primeirotermo + (c-1)) * razao
    print(soma, end=" -> ")
    c += 1
termosmais = int(input('Quantos termos mais você deseja ver? '))
while termosmais != 0:
    termosmais += c
    while c < termosmais:
        soma = (primeirotermo + (c - 1)) * razao
        print(soma, end=" -> ")
        c += 1
    termosmais = 0
    termosmais = int(input('Deseja ver mais? Quantos? '))
print('FIM')