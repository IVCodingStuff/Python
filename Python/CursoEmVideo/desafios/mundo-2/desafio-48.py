s = int()
for c in range(0,500):
    if c % 3 == 0 and c % 2 != 0:
        s += c
print('Soma dos números ímpares e múltiplos de três entre 1 e 500: {}'. format(s))