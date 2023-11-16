import mysql.connector
banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='302302',
    database='academia_turma_d')
cursor = banco.cursor()
