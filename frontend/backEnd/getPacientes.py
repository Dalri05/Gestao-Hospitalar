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

def getAllPacientes():
    cursor.execute('select nome, idade, sexo, CEP, telefone from pacientes')
    nomes = cursor.fetchall()
    print (nomes)
    return nomes
    