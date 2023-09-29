numtot = int(input('Quantos eleitores votaram? '))
votbra = int(input('Quantos votaram branco? '))
votnul = int(input('Quantos votaram nulo? '))
votval = int(input('Quantos votos são válidos?'))

porcembra = (votbra/numtot)*100
porcemnul = (votnul/numtot)*100
porcemval = (votval/numtot)*100

print ('Votos brancos: {}%\n Votos nulos: {}% \n Votos válidos: {}%'.format(porcembra,porcemnul,porcembra) )
