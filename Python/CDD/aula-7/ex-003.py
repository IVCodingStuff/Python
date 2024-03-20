#num = int(input('Insira um número: '))
#for c in range(num+1):
#    for a in range(1,c+1):
#        print(a, end= '')
#    print('')
c = 1
num = int(input('Insira um número: '))
while c <= num:
    a=1
    while a <= c:
        print(a,end='')
        a += 1
    print()
    c +=1
