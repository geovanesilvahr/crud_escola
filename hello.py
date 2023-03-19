from flask import Flask, url_for
from flask import render_template
import sqlite3

#Instanciando a aplicação
app = Flask(__name__)

#Criando o Bando de Dados
connectionDB = sqlite3.connect("db/database.db")
cursor = connectionDB.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS  alunos(
        matricula INT, 
        p_nome VARCHAR(15),
        s_nome VARCHAR(40),
        email VARCHAR(80),
        data_nasc INT,
        cpf INT
        )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS end(
        matricula INT,
        logradouro VARCHAR(80),
        numero INT,
        cep INT
    )
""")    
@app.route('/')
@app.route('/<name>')
def hello(name='Geovane'):
    return render_template('cadAlunos.html', name=name)

def inserir(form):
    cursor.executemany("""
        INSERT INTO alunos VALUES(?, ?, ?, ?)
    """, form)
    return print("Inseriu!")

