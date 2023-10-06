nomes = [0]*5
for c in range(5):
    nomes[c] = input('{} nome: '.format(c+1))
print(nomes)
for d in range(5,1,-1):
    print (nomes[d],end ="\n")