from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('gestao_hospitalar.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER,
               sexo TEXT,
               cpf TEXT UNIQUE,
               endereco TEXT,
               telefone TEXT
    )
''')

conn.commit()
conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('gestao_hospitalar.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pacientes')
    pacientes = cursor.fetchall()
    conn.close()
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

        conn = sqlite3.connect('gestao_hospitalar.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pacientes (nome, idade, sexo, cpf, endereco, telefone)
            VALUES (?, ?, ?, ?, ?, ?)
''', (nome, idade, sexo, cpf, endereco, telefone))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('novo_paciente.html')

@app.route('/limpar_pacientes')
def limpar_pacientes():
    conn = sqlite3.connect('gestao_hospitalar.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pacientes')
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/agendar_consulta')
def agendar_consulta():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        data = request.form['data']
        consulta = request.form['consulta']

        conn = sqlite3.connect('gestao_hospitalar.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pacientes (nome, cpf, data, consulta)
            VALUES (?, ?, ?, ?)
''', (nome, cpf, data, consulta))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('consulta.html')

@app.route('/ver_consultas')
def agendar_consulta():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        data = request.form['data']
        consulta = request.form['consulta']

        conn = sqlite3.connect('gestao_hospitalar.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pacientes (nome, cpf, data, consulta)
            VALUES (?, ?, ?, ?)
''', (nome, cpf, data, consulta))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('visconsultas.html')

if __name__ == '__main__':
    app.run(debug=True)
