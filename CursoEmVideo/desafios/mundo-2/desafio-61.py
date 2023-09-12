soma = int()
primeirotermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
c = 1
while c <= 10:
    soma = (primeirotermo + (c-1)) * razao
    print(soma, end=" -> ")
    c += 1
print('FIM')