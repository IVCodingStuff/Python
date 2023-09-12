anonasc = int(input('Em que ano você nasceu? '))
anoatual = 2023
idade = anoatual - anonasc

if idade - 18 == 0:
    print ('É hora de você se alistar!') 
elif idade - 18 < 0:
    print ('Ainda não é hora de você se alistar. Faltam {} anos para você poder se juntar as forças.'.format(abs(idade - 18)))
else:
    print('Já passou do prazo para se alistar. Você poderia ter se candidatado há {} anos.'.format(abs(idade-18)))
