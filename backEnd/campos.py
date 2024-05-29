from app import *
import mysql.connector
from flask import request

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="gestaohospitalar"
    )
    cursor = conexao.cursor()
except mysql.connector.Error as err:
    print("Erro de conexão com o banco de dados:", err)
    exit(1)

def queryCampo():
    cursor.execute('SELECT nome FROM usuarios')
    nomes = [registro[0] for registro in cursor.fetchall()]
    logNome = " / ".join(nomes)
    print("usuatios encontrados" + logNome)
    return nomes

def confereCpf():
    cpf = request.form['cpf']
    cursor.execute('SELECT cpf FROM usuarios WHERE cpf = %s', (cpf,))
    cpfConferido = [registro[0] for registro in cursor.fetchall()]
    logNome = " / ".join(cpfConferido)
    print("usuatios encontrados" + logNome)
    return cpfConferido
