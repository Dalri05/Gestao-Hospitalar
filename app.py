from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from backEnd.campos import *

app = Flask(__name__)
app.secret_key = '12345'
senhaAdmin = '12345'

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

@app.route('/inicio')
def index():
    cursor.execute('SELECT * FROM pacientes')
    pacientes = cursor.fetchall()
    return render_template('index.html', pacientes=pacientes)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        try:
            cursor.execute('''
            INSERT INTO usuarios (usuario, senha, nome, cpf, email)
            VALUES (%s, %s, %s, %s, %s)''', (usuario, senha, nome, cpf, email))
            conexao.commit()
            return redirect(url_for('login'))
        except:
            flash('CPF ou usuario ja existente em nossa base de dados')
    
    return render_template('cadastro.html')



@app.route('/novo_paciente', methods=['GET', 'POST'])
def novo_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        sexo = request.form['sexo']
        cpf = request.form['cpf']
        cep = request.form['cep']
        telefone = request.form['telefone']

        cursor.execute('''
            INSERT INTO pacientes (nome, idade, sexo, cpf, cep, telefone)
            VALUES (%s, %s, %s, %s, %s, %s)''', (nome, idade, sexo, cpf, cep, telefone))
        conexao.commit()
        return redirect(url_for('index'))
    return render_template('novo_paciente.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username'].strip()
        senha = request.form['password'].strip()

        cursor.execute('SELECT * FROM usuarios WHERE usuario = %s', (usuario,))
        usuario_encontrado = cursor.fetchone()

        if usuario_encontrado:
            # Para depuração: exibir o hash da senha armazenada
            print(f"Senha armazenada (hash): {usuario_encontrado[1]}")
            print(f"Senha fornecida: {senha}")

            if check_password_hash(usuario_encontrado[1], senha):
                return redirect(url_for('index'))
            if {senha} == senhaAdmin:
                return redirect(url_for('index'))
            else:
                flash('Senha incorreta', 'error')
        else:
            flash('Usuário não encontrado', 'error')

    return render_template('login.html')


@app.route('/limpar_pacientes')
def limpar_pacientes():
    cursor.execute('DELETE FROM pacientes')
    conexao.commit()
    return redirect(url_for('index'))

@app.route('/agendar_consulta', methods=['GET', 'POST'])
def agendar_consulta():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        data = request.form['data']
        consulta = request.form['consulta']

        cursor.execute('''
            INSERT INTO consultas (nome, cpf, data, consulta)
            VALUES (%s, %s, %s, %s)
''', (nome, cpf, data, consulta))
        conexao.commit()
        return redirect(url_for('index'))
    return render_template('consulta.html')

@app.route('/ver_consultas')
def ver_consultas():
    cursor.execute('SELECT * FROM consultas')
    consultas = cursor.fetchall()
    return render_template('visconsultas.html', consultas=consultas)

@app.route('/camposNome')
def camposNome():
    nomes = queryCampo()
    return jsonify(nomes)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
