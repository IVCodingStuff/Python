from biblio_banco import *

def cadastrar_aluno(nome, cpf, telefone, email, endereco):
    cadastro_aluno = 'insert into alunos (nome, cpf, telefone, email, endereco) values (%s, %s, %s, %s,%s);'
    data = (nome, cpf, telefone, email, endereco)
    cursor.execute(cadastro_aluno, data)
    banco.commit()
def deletar_aluno(matricula):
    deletar_aluno = (f'delete from alunos where matricula = {matricula};')
    data_matricula = (matricula, )
    cursor.execute(deletar_aluno)
def consultar_alunos():
    consulta_alunos = 'select * from alunos;'
    cursor.execute(consulta_alunos)

def cadastrar_funcionario(id_funcionario,nome, cpf_funcionario, departamento, salario, filhos):
    cadastro_funcionario = 'insert into func (id_funcionario,nome, cpf_funcionario, departamento, salario, filhos) values (%s, %s, %s, %s,%s, %s);'
    data = (id_funcionario,nome, cpf_funcionario, departamento, salario, filhos)
    cursor.execute(cadastro_funcionario, data)
    banco.commit()
def deletar_funcionario(id_funcionario):
    data = id_funcionario
    deletar_funcionario = ('delete from func where id_funcionario = (%s);')
    cursor.execute(deletar_funcionario,data)
def consultar_funcionario():
    consulta_funcionario = 'select * from func;'
    cursor.execute(consulta_funcionario)
def cadastrar_modalidade(nome):
    cadastro_modalidade = 'insert into modalidades (nome) values (%s);'
    data = (nome)
    cursor.execute(cadastro_modalidade, data)
    banco.commit()

def deletar_modalidade(id_modalidade):
    data = id_modalidade
    deletar_modalidade = ('delete from modalidades where id_modalidade = (%s);')
    cursor.execute(deletar_modalidade, data)

def consultar_modalidade():
    consulta_modalidade = 'select * from modalidades;'
    cursor.execute(consulta_modalidade)

def cadastrar_personal(cpf, cref, nome, telefone, email):
    cadastro_personal = 'insert into personal (cpf, cref, nome, telefone, email) values (%s, %s, %s, %s,%s);'
    data = (cpf, cref, nome, telefone, email)
    cursor.execute(cadastro_personal, data)
    banco.commit()

def deletar_personal(cpf):
    data = cpf
    deletar_personal = ('delete * from personal where cpf = (%s);')
    cursor.execute(deletar_personal, data)

def consultar_personal():
    consulta_personal = 'select * from personal;'
    cursor.execute(consulta_personal)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

def sair_programa():
    print('Sistema Finalizado')
    cursor.close()
    banco.close()


