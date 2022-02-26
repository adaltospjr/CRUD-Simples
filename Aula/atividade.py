from flask import Flask, render_template, request
import conexao

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('escopo.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    conexao.gravar(nome,email,senha)

    dados = conexao.consulta()

    return str(dados)

@app.route('/consultar')
def consultar():
    dados = conexao.consulta()
    return str(dados)

app.run()
