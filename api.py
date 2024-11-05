import requests
import mysql.connector
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turma_c"
)
cep = input("Qual o cep?")
meucursor=banco.cursor()
if len(cep)==8:
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao=requests.get(link)
    print(requisicao)
    dic_requisicao = requisicao.json()

    cep = dic_requisicao['cep']
    logradouro = dic_requisicao['logradouro']
    complemento = dic_requisicao['complemento']
    print(dic_requisicao)

    meucursor = banco.cursor()
    sql = "insert into enderecos (cep,logradouro,complemento) values(%s,%s,%s)"
    data = (cep, logradouro, complemento)
    meucursor.execute(sql, data)
    banco.commit()

meucursor.close()
banco.close()


