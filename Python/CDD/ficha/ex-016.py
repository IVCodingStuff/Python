inicio = int(input('Horário de início: '))
fim = int(input('Horário de finalização: '))
if fim < inicio:
    tempo = (24 - inicio) + fim
    print(tempo)
else:
    tempo = fim - inicio
    print(tempo)