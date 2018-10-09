from app.model import *
import os 

if __name__ == "__main__":

    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([
        Aluno,
        Area,
        Docente,
        Docente.areas.get_through_model(),
        TrabalhoPI,
        TrabalhoPI.alunos.get_through_model(),
        TrabalhoPI.docentes.get_through_model()])

    pedro = Aluno.create(nome = "Pedro de Oliveira", 
        turma = "301 INFO")
    maria = Aluno.create(nome = "Maria de Souza", 
        turma = "301 INFO")

    bd = Area.create(nome = "Banco de dados",
        descricao = "Modelagem, implementação e "+\
        "suporte de bancos de dados.")
    tf = Area.create(nome = "Tolerância a faltas", 
        descricao = "Provimento de robustez a sistemas, "+\
        "para que os mesmos operem de maneira ininterrupta.")
    
    aldelir = Docente.create(nome = "Aldelir Luiz")
    aldelir.areas.add(bd)
    aldelir.areas.add(tf)

    t1 = TrabalhoPI.create(titulo = "Bancos de Dados em "+\
        "Grafos para Modelagem Tridimensional de Estrelas",
        descricao = "Uso do Neo4j para armazenar "+\
        "pontos da estrela Órion",
        url = "não disponível")
    t1.alunos.add(pedro)
    t1.alunos.add(maria)
    t1.docentes.add(aldelir)

    print(t1)   
    print(Aluno.select()[0])