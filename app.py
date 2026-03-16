from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco e criar a tabela se não existir
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    # Busca todos os clientes para exibir na tela
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return render_template('index.html', clientes=clientes)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')

    if nome and email:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", 
                       (nome, email, telefone))
        conn.commit()
        conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)