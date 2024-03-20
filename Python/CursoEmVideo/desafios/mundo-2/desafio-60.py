num = int(input('Insira um número: '))
fat = num
numfat = 1
while fat != 1:
    numfat = numfat * fat
    fat -= 1
print ('{}! = {}'.format(num, numfat))
