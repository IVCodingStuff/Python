notas = [0]*5
maior = 0
media = 0
for c in range (5):
    notas[c] = int(input('Nota do {}º aluno: '.format(c+1)))

for d in range (5):
    media += notas[d]
media = media/5

for e in range(5):
    if notas[e] >= media:
        maior += 1

print('A média da turma foi {} e {} alunos a atigiram ou ultrapassaram.'.format(media, maior))