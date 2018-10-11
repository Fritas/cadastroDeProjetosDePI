from flask import Flask, render_template, redirect, request
from model import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

# ---------------------------------------------------
# PROJETOS
# ---------------------------------------------------
@app.route('/projetos')
def exibir_projetos():
    dic = {
        'titulo' : 'Projetos',
        'link_exibir' : 'projetos/projeto',
        'itens' : TrabalhoPI.select()
    }
    return render_template('listar.html', dic=dic)

@app.route("/projetos/projeto/", methods=["GET"])
def exibir_projeto():    
    try:
        projeto_id = request.args.get('id')
    except Exception as identifier:
        print("\n\nErro em exibir_projeto: %s \n" %(identifier))
        return error(mensagem="Página não encontrada!")
    else:
        try:
            #POSICAO 0, POIS O PEEWEE DEVOLVE UMA LISTA
            projeto = TrabalhoPI.select().where(TrabalhoPI.id == projeto_id)[0]
        except Exception as identifier:
            print("\n\nErro em exibir_projeto: %s \n" %(identifier))
            return error(mensagem="Projeto não encontrado!")
        else:
            dic = {
                'titulo' : projeto.titulo,
                'projeto' : projeto,
                
            }
            return render_template("projeto_exibir.html", dic=dic)

@app.route("/projeto/cadastrar")
def cadastrar_projeto():
    dic = {}
    return render_template('projeto_cadastrar.html', dic=dic)

# ---------------------------------------------------
# DOCENTES
# ---------------------------------------------------
@app.route('/docentes')
def exibir_docentes():
    dic = {
        'titulo' : 'Docentes',
        'link_exibir' : 'docentes/docente',
        'itens' : Docente.select()
    }
    return render_template('listar.html', dic=dic)

@app.route("/docentes/docente/", methods=["GET"])
def exibir_docente():    
    try:
        docente_id = request.args.get('id')
    except Exception as identifier:
        print("\n\nErro em exibir_docente: %s \n" %(identifier))
        return error(mensagem="Página não encontrada!")
    else:
        try:
            #POSICAO 0, POIS O PEEWEE DEVOLVE UMA LISTA
            docente = Docente.select().where(Docente.id == docente_id)[0]
        except Exception as identifier:
            print("\n\nErro em exibir_docente: %s \n" %(identifier))
            return error(mensagem="Docente não encontrado!")
        else:
            dic = {
                'docente' : docente,
            }
            return render_template("docente.html", dic=dic)

# ---------------------------------------------------
# ALUNOS
# ---------------------------------------------------
@app.route('/alunos')
def exibir_alunos():
    dic = {
        'titulo' : 'Alunos',
        'link_exibir' : 'alunos/aluno',
        'link_cadastrar' : 'alunos/cadastrar',
        'itens' : Aluno.select()
    }
    return render_template('listar.html', dic=dic)

@app.route("/alunos/aluno/", methods=["GET"])
def exibir_aluno():    
    print("Exibir aluno")
    try:
        aluno_id = request.args.get('id')
        print("\n\nAluno id:  ", aluno_id)
    except Exception as identifier:
        print("\n\nErro em exibir_aluno: %s \n" %(identifier))
        return error(mensagem="Página não encontrada!")
    else:
        try:
            #POSICAO 0, POIS O PEEWEE DEVOLVE UMA LISTA
            aluno = Aluno.select().where(Aluno.id == aluno_id)[0]
        except Exception as identifier:
            print("\n\nErro em exibir_aluno: %s \n" %(identifier))
            return error(mensagem="Aluno não encontrado!")
        else:
            dic = {
                'aluno' : aluno,
            }
            return render_template("aluno_exibir.html", dic=dic)

@app.route('/alunos/cadastrar')
def cadastrar_aluno():
    return render_template('aluno_cadastrar.html')

# ---------------------------------------------------
# ERROS
# ---------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html'), 404

def error(mensagem=""):
    return render_template('error.html', mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)

