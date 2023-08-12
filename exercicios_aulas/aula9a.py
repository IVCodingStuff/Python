frase = "vish kk"
print (frase[9:0:-1])
#[9] - 1 caractere
#[2:9] - vai do 2 até o 8
#[2:9:2] - vai do 2 até 8 pulando de dois em dois
#[:5] - vai do começo até o 4
#[15:] - vai do 15 até o fim
#[9::3] - vai do 9 até o fim pulando de três em três

#len(frase) - comprimento da frase
#frase.count('i') - quantas vezes aparece certa letra
#frase.count('i,0,13') - "" do zero até o 12
#frase.find('kk') - onde encontrou a(s) letra(s) indicadas (se não houver, ele responde -1)

#'kk' in frase - procura na frase e responde True ou False 
#frase.replace ('vish','tá bom') - troca um pelo outro
#frase.upper() - deixa tudo que é mminusculo pra maiusculo
#frase.upper() - deixa tudo maiusculo minusculo
#frase.capitalize() - Só o primeiro caractere maiusculo e o resto minusculo
#frase.title() - Todas as primeiras letras em maiusculos
#frase.strip() - remove espaços no inicio e fim da string
#frase.rstrip() - remove espaços na direita
#frase.lstrip() - remove espaços na esquerda

#frase.split() - Divide a string pelos espaços e as coloca numa lista

#'-'.join(frase) - Junta as string e coloca o caractere informado entre elas
#"""Essa frase vai ficar
#separada, se usar três aspas"""