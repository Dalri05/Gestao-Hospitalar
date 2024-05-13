from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

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

@app.route('/')
def index():
    cursor.execute('SELECT * FROM pacientes')
    pacientes = cursor.fetchall()
    return render_template('index.html', pacientes=pacientes)

@app.route('/novo_paciente', methods=['GET', 'POST'])
def novo_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        sexo = request.form['sexo']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        telefone = request.form['telefone']

        cursor.execute('''
            INSERT INTO pacientes (nome, idade, sexo, cpf, endereco, telefone)
            VALUES (%s, %s, %s, %s, %s, %s)
''', (nome, idade, sexo, cpf, endereco, telefone))
        conexao.commit()
        return redirect(url_for('index'))
    return render_template('novo_paciente.html')

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

if __name__ == '__main__':
    app.run(debug=True, port=8000)
