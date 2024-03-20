from biblio_banco import *
import os
cursor = banco.cursor()

def cadastrar_aluno(nome, cpf, telefone, email, endereco):
    cadastro_aluno = 'insert into alunos (nome, cpf, telefone, email, endereco) values (%s, %s, %s, %s,%s);'
    data = (nome, cpf, telefone, email, endereco)
    cursor.execute(cadastro_aluno, data)
    banco.commit()
    os.system('cls')
    print('\nAlunx cadastradx com sucesso.')

def deletar_aluno(matricula):
    deletar = f'DELETE FROM alunos WHERE matricula = "{matricula}"'
    cursor.execute(deletar)
    banco.commit()
    os.system('cls')
    print('\nAlunx deletadx com sucesso.')

def consultar_alunos():
    print('')
    consulta_personal = 'SELECT * FROM alunos;'
    cursor.execute(consulta_personal)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)
    
def cadastrar_funcionario(nome, cpf_funcionario, departamento, salario, filhos):
    cadastro_funcionario = 'insert into func (nome, cpf_funcionario, departamento, salario, filhos) values (%s, %s, %s,%s, %s);'
    data = (nome, cpf_funcionario, departamento, salario, filhos)
    cursor.execute(cadastro_funcionario, data)
    banco.commit()
    os.system('cls')
    print('Funcionárix cadastradx com sucesso.')

def deletar_funcionario(id_funcionario):
    deletar = f'DELETE FROM func WHERE id_funcionario = "{id_funcionario}"'
    cursor.execute(deletar)
    banco.commit()
    os.system('cls')
    print('Funcionárix deletadx com sucesso.')

def consultar_funcionario():
    print('\n')
    consulta_funcionario = 'SELECT * FROM func;'
    cursor.execute(consulta_funcionario)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

def cadastrar_modalidade(nome):
    cadastro_modalidade = f'INSERT into modalidades (nome) VALUES ("{nome}");'
    cursor.execute(cadastro_modalidade)
    banco.commit()
    os.system('cls')
    print('\nModalidade cadastrada com sucesso.')

def deletar_modalidade(id_modalidade):
    deletar = f'DELETE FROM modalidades WHERE id_mod = "{id_modalidade}"'
    cursor.execute(deletar)
    banco.commit()
    os.system('cls')
    print('Modalidade deletada')

def consultar_modalidade():
    print('\n')
    consulta_modalidade = 'SELECT * FROM personal;'
    cursor.execute(consulta_modalidade)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

def cadastrar_personal(cpf, cref, nome, telefone, email):
    cadastro_personal = 'insert into personal (cpf, cref, nome, telefone, email) values (%s, %s, %s, %s,%s);'
    data = (cpf, cref, nome, telefone, email)
    cursor.execute(cadastro_personal, data)
    banco.commit()
    os.system('cls')
    print('Personal cadastradx com sucesso.')

def deletar_personal(cpf):
    deletar = f'DELETE FROM personal WHERE cpf = "{cpf}"'
    cursor.execute(deletar)
    banco.commit()
    os.system('cls')
    print('Personal deletadx com sucesso.')

def consultar_personal():
    print('\n')
    consulta_personal = 'SELECT * FROM personal;'
    cursor.execute(consulta_personal)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

def sair_programa(continuar):
    continuar = False
    os.system('cls')
    print('\nSistema Finalizado')
    cursor.close()
    banco.close()
    return continuar

