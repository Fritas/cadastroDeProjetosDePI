from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
db = SQLAlchemy(app)

class Autor(db.Model):    
    """
    Esta classe implementa um objeto Autor

    :type id: int
    :type primeiro_nome: string
    :type nome_do_meio: string
    :type ultimo_nome: string
    :type data_de_nascimento: datetime
    :type CPF: string
    """


    id = db.Column(db.integer, primary_key=True)
    primeiro_nome = db.Column(db.String(15))
    nome_do_meio = db.Column(db.String(30), nullable=True) #nullable=True permiti null
    ultimo_nome = db.Column(db.String(15))
    data_de_nascimento = db.Column(db.String(15))
    CPF = db.Column(db.String(15), unique=True)

    def validar_cpf(self, cpf):
        """
        :type CPF: string
        """
        pass

    def atualizar_nome(self, n_primeiro_nome, n_nome_do_meio, n_ultimo_nome):
        """
        :type primeiro_nome: string
        :type nome_do_meio: string
        :type ultimo_nome: string
        """
        pass

    def _str__(self):
        pass

class Projeto(db.Model):
    """ """


    def __init__(self, titulo, autores, descricao="", id=None):
        """
        :type id: int
        :type titulo: string
        :type lista_autores: list
        :type descricao: string
        :type lista_orientadores: list
        :type lista_coorientadores: list
        :type lista_colaboradores: list
        """
        pass

    def adicionar_autor(self, autor):
        """
        :type autor: Autor
        """
        pass

    def adicionar_orientador(self, orientador):
        """
        :type orientador: Autor
        """
        pass

    def adicionar_coorientador(self, coorientador):
        """
        :type coorientador: Autor
        """
        pass
    def adicionar_colaborador(self, colaborador):
        """
        :type colaborador: Autor
        """
        pass

    def _str__(self):
        pass