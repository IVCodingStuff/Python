hora1 = int(input('Hora 1:'))
minutos1 = int(input('Minutos 1:'))
hora2 = int(input('Hora 1:'))
minutos2 = int(input('Minutos 2:'))
horafinal = 0
minutosfinal = minutos1 + minutos2
if minutosfinal >= 60:
    horafinal += 1
    minutosfinal -= 60
horafinal += (hora1 + hora2)
if horafinal > 12:
    horafinal -= 12
print('{}:{}'.format(horafinal,minutosfinal))