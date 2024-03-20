from biblio_opcoes import *
from biblio_banco import *
import os

continuar = True
while continuar:
    print('\n=== ACADEMIA CDD ===\n\n1. Alunes\n2. Modalidades\n3. Funcionaries\n4. Personal\n5. Sair')
    opcao = int(input('\nQual tabela deseja acessar? '))
    os.system('cls')
    if opcao == 1:
        print('ALUNOS\n\n1.Cadastrar alunx\n2.Deletar alunx\n3.Mostrar tabela\n4.Voltar')
        opcao2 = int(input('\nO que deseja fazer? '))
        os.system('cls')
        if opcao2 == 1:
            print('\nINFORMAÇÕES DX ALUNX\n')
            nome = input('Nome: ')
            cpf = input('CPF: ')
            telefone = input('Telefone: ')
            email = input('Email: ')
            endereco = input('Endereço: ')
            cadastrar_aluno(nome, cpf, telefone, email, endereco)
        elif opcao2 == 2:
            print('\nDESLIGAMENTO DE ALUNX')
            matricula = int(input('\nInsira a matrícula dx alunx: '))
            deletar_aluno(matricula)
        elif opcao2 == 3:
            print('\nTABELA ALUNOS')
            consultar_alunos()
        elif opcao2 == 4:
            print('')
            os.system('cls')


    elif opcao == 2:
        print('MODALIDADE\n\n1.Cadastrar modalidade\n2.Deletar modalidade\n3.Mostrar tabela\n4.Voltar')
        opcao2 = int(input('\nO que deseja fazer? '))
        if opcao2 == 1:
            print('\nINFORMAÇÕES DA MODALIDADE\n')
            nome = input('Nome: ')
            cadastrar_modalidade(nome)
        elif opcao2 == 2:
            print('\nFINALIZAÇÃO DE MODALIDADE')
            id_modalidade = int(input('Insira o ID da modalidade: '))
            deletar_modalidade(id_modalidade)
        elif opcao2 == 3:
            print('\nTABELA MODALIDADES')
            consultar_modalidade()
        elif opcao2 == 4:
            print('')
            os.system('cls')

    elif opcao == 3:
        print('FUNCIONÁRIXS\n\n1.Cadastrar funcionário\n2.Deletar funcionário\n3.Mostrar tabela\n4.Voltar')
        opcao2 = int(input('\nO que deseja fazer? '))
        os.system('cls')
        if opcao2 == 1:
            print('\nINFORMAÇÕES DX FUNCIONÁRIX\n')
            nome = input('Nome: ')
            cpf_funcionario = input('CPF: ')
            departamento = int(input('Departamento: '))
            salario = float(input('Salário: '))
            filhos = int(input('Filhos: '))
            cadastrar_funcionario(nome, cpf_funcionario, departamento, salario, filhos)
        elif opcao2 == 2:
            print('\nDESLIGAMENTO DE FUNCIONÁRIO')
            id_funcionario = int(input('Insira o ID dx funcionarix: '))
            deletar_funcionario(id_funcionario)
        elif opcao2 == 3:
            print('\nTABELA FUNCIONÁRIOS')
            consultar_funcionario()
        elif opcao2 == 4:
            print('')
            os.system('cls')

    elif opcao == 4:
        print('PERSONALS\n\n1.Cadastrar personal\n2.Deletar personal\n3.Mostrar tabela\n4.Voltar')
        opcao2 = int(input('\nO que deseja fazer? '))
        if opcao2 == 1:
            print('\nINFORMAÇÕES DX PERSONAL\n')
            cpf = input('CPF: ')
            cref = input('CREF: ')
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            email = input('Email: ')
            cadastrar_personal(cpf, cref, nome, telefone, email)
        elif opcao2 == 2:
            print('\nFINALIZAÇÃO DX PERSONAL')
            cpf = int(input('Insira o CPF dx personal: '))
            deletar_personal(cpf)
        elif opcao2 == 3:
            print('\nTABELA PERSONAL')
            consultar_personal()
        elif opcao2 == 4:
            print('')
            os.system('cls')
    elif opcao == 5:
        continuar = sair_programa(continuar)
        

