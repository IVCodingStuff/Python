a = [0]*3
x = int(input('Insira um número: '))
m = [0]*3
for b in range (3):
    a[b] = int(input('Digite um número:'))
for c in range (3):
    m[c] = a[c]*x

print (m)