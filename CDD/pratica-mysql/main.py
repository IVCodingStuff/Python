from biblio_opcoes import *

while True:
    print('=== ACADAMIA CDD ===\n\n1.Alunes\n2.Modalidades\n3.Funcionarios\n4.Personal\n5. Sair')
    opcao = int(input('Qual tabela deseja acessar?'))

    if opcao == 1:
        print('1.Cadastrar alunx\n2.Deletar alunx\n3.Mostrar tabela\n4.Voltar')
        opcao2 = int(input('O que deseja fazer? '))
        if opcao2 == 1:
            print('\nINFORMAÇÕES DX ALUNX\n')
            nome = input('Nome: ')
            cpf = input('CPF: ')
            telefone = input('Telefone: ')
            email = input('Email: ')
            endereco = input('Endereço: ')
            cadastrar_aluno(nome, cpf, telefone, email, endereco)
        elif opcao2 == 2:
            print('DESLIGAMENTO DE ALUNX')
            matricula = int(input('Insira a matrícula dx alunx: '))
            deletar_aluno(matricula)
        elif opcao2 == 3:
            print('TABELA ALUNOS')
            consultar_alunos()

    elif opcao == 2:
        print('1.Cadastrar modalidade\n2.Deletar modalidade\n3.Mostrar tabela\n4.Voltar')
        opcao2 = int(input('O que deseja fazer? '))
        if opcao2 == 1:
            print('\nINFORMAÇÕES DA MODALIDADE\n')
            nome = input('Nome: ')
            cadastrar_modalidade(nome)
    elif opcao == 3:
        print('1.Cadastrar funcionário\n2.Deletar funcionário\n3.Mostrar tabela\n4.Voltar')
        opcao2 = int(input('O que deseja fazer? '))
    elif opcao == 4:
        print('1.Cadastrar personal\n2.Deletar personal\n3.Mostrar tabela\n4.Voltar')
        opcao2 = int(input('O que deseja fazer? '))
    elif opcao == 5:
        print('1.Cadastrar alunx\n2.Deletar alunx\n3.Mostrar tabela\n4.Voltar')
        opcao2 = int(input('O que deseja fazer? '))

