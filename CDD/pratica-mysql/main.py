import mysql.connector
banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='302302',
    database='academia_turma_d')
cursor = banco.cursor()
pesquisa = 'select * from func;'
cursor.execute(pesquisa)
resultado = cursor.fetchall()
for x in resultado:
    print(x)

nome1= 'menino Gay'
telefone1 ='81924242424'
sql = 'insert into alunos (nome, telefone) values (%s, %s)'
data = (nome1, telefone1)
cursor.execute(sql,data)
banco.commit()
'''userid = cursor.lastrowid
print(userid)
'''
cursor.close()
banco.close()


