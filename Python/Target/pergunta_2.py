objetivo = int(input("Insira um número: "))

num = 0
num2 = 1
print(num)
while num2 <= objetivo:
    print(num2)
    num, num2 = num2, num + num2
    if num2 == objetivo:
        print('O número {} pertence a sequência'.format(objetivo))
        break
    if num2 > objetivo:
        print('O número {} não pertence a sequência'.format(objetivo))
        break
