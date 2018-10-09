from flask import Flask, render_template, redirect, request
from model import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/projetos/')
def projetos():
    try:
        projeto_id = request.args.get('id')
    except Exception as identifier:
        print(identifier)
        dic = {
            'titulo' : 'Projetos',
            'link' : 'projeto',
            'itens' : TrabalhoPI.select()
        }
        return render_template('listar.html', dic=dic)
    else:
        projeto = TrabalhoPI.select().where(TrabalhoPI.id == projeto_id)
        dic = {
            'titulo' : projeto.titulo,
            'projeto' : projeto,
        }
        return render_template('projeto.html', dic=dic)

@app.route("/projeto/inserir")
def inserir_projeto():
    dic = {
        'titulo' : 'Inserir',
        'itens' : TrabalhoPI.select()
    }
    return render_template('listar.html', dic=dic)

@app.route('/docentes')
def docentes():
    dic = {
        'titulo' : 'Docentes',
        'itens' : Docente.select()
    }
    return render_template('listar.html', dic=dic)

@app.route('/alunos')
def alunos():
    dic = {
        'titulo' : 'Alunos',
        'itens' : Aluno.select()
    }
    return render_template('listar.html', dic=dic)

if __name__ == "__main__":
    app.run(debug=True)
