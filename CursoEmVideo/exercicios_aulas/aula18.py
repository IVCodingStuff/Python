pessoas = [['Maria', 50],['Carlos',20],['Joaquim', 37]]
print(pessoas[0][0]) #Maria
print(pessoas[2][1]) #37
info = list()
info.append(pessoas[:]) #Adiciona uma cópia da lista atual
info.append(pessoas) #Muda os dados dentro de (info) se (pessoas) mudar, pois é criada uma ligação entre elas
for p in range (len(pessoas)):
    print(pessoas[0])
