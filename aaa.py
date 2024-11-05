import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turma_c"
)
meucursor=banco.cursor()
pesquisa='select * from alunos;'
meucursor.execute(pesquisa)
# fetchall recebe tudo da pesquisa e retorna através de uma tupla
resultado=meucursor.fetchall()
for x in resultado:
    print(x)

nome1=input ("Digite o nome do aluno")
telefone1=input ("Digite o telefone do aluno")

sql = "INSERT INTO alunos (nome, telefone) VALUES (%s, %s)"
data = (nome1, telefone1)
meucursor.execute(sql,data)
banco.commit()

meucursor.close()
banco.close()