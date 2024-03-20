maipeso = float()
menpeso = float()
for c in range(1,6):
    peso = float(input('Peso da {}º pessoa: '.format(c)))
    if peso > maipeso:
        maipeso  = peso
    if c == 1:
        menpeso = peso 
    if peso < menpeso:
        menpeso  = peso
print('O maior peso lido foi de {}Kg.'.format(maipeso))
print('O menor peso lido foi de {}Kg.'.format(menpeso))