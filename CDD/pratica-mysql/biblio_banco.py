import mysql.connector
banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='235100',
    database='academia_turma_d'
    )
cursor = banco.cursor()

cursor.execute("SELECT * FROM alunos")
myresult = cursor.fetchall()
for x in myresult:
  print(x)
