soma = int()
primeirotermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
c = 1
for c in range(1,11):
    soma = (primeirotermo + (c-1)) * razao
    print(soma, end=" -> ")
    c += 1
print('FIM')