import random
n = random.randint (1,5)

print ('Advinhe o número que pensei! É um de 1 a 5.')
nu = int(input('Acho que você pensou em '))
if nu == n:
    print('Boa! Você acertou.')
else:
    print('Nah, eu pensei em {}'.format(n))