nome = [0]*5
senha = [0]*5
logado = 0
semcadastro = 0
while True:
    for x in range (5):
        nome[x] = input('Nome: ')
        senha[x] = input('Senha: ')
        print('')
    print('===============================')
    print('          Login')
    print('===============================')
    nomeLogin = input('Usuário: ')
    senhaLogin = input('Senha: ')
    for z in range(5):
        if nomeLogin == nome[z] and senhaLogin == senha[z]:
            logado += 1
    if logado == 1:
        print('Login efetuado com sucesso!')
    else:
        print('Usuário ou senha incorretos.')
