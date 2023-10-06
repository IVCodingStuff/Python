media = 0
maior = 0
num = [0]*5
for c in range(5):
    num[c] = int(input('Insira o {}º número: '.format(c+1)))
for d in range(5):    
    if num[d] % 2 == 0:
        print(num)
    if num[d] > maior:
        maior = num[d]
        media += num[d]