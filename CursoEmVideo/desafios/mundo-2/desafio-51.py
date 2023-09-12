s = int()
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
r -= pt
for c in range(1,11):
    s = c
    s = pt + (c-1) * r
    print (s)