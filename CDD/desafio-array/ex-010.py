n = [0]*30
encontrado = 0
for c in range(30):
    n[c] = float(input('{}º número: '.format(c+1)))
procura = float(input('Qual número deseja encontrar? '))
for d in range(30):
    if procura == n[d]:
        encontrado += 1
print('{} aparece {} vezes dentro do vetor.'.format(procura, encontrado))