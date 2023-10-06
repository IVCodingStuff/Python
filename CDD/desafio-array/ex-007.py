nome = [0]*5
senha = [0]*5
for x in range (5):
    nome[x] = input('Nome:')
    senha[x] = input('Senha: ')
    print('')
for z in range (5):
    print('{}. Nome: {}\nSenha: {}\n'. format(z, nome[z], senha[z]))