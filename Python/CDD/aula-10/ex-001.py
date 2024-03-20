numAl = int(input('Quantos alunos tem na sala? '))
nomes = ['']*numAl
encontrado = 0
for c in range (numAl):
    nomes[c] = input('Nome do aluno: ')
#for d in range (numAl):
#    print(('{}. {}').format(d,nomes[d]))
procura = input('Quem quer encontrar? ')
for d in range (numAl):
    if nomes[d] == procura:
        print(('{}. {}').format(d, nomes[d]))
        encontrado += 1
if encontrado == 0:
    print ('Nome não encontrado')