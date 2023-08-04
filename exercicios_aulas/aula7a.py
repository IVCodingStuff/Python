#/n - quebra linha
#/end = '' - na mesma linha
n1 = int(input('Dê um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d1 = n1 // n2
e = n1 ** n2
print ('A soma é {}\n, a multiplicação é {}, \n a divisão é {:.3f}.'.format(s, m, d), end ='')
print (' Divisão inteira {} e potência {}'.format(d1, e))
