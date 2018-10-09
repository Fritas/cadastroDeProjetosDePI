from datetime import date
from app.model import Autor

autor = Autor(
    primeiro_nome = 'Adriano',
    nome_do_meio = 'Damasceno da Silva',
    ultimo_nome = 'Júnior',
    data_de_nascimento = date(year=2000, month=6, day=21),
    CPF= "000.000.000-00"
)

#autor = Autor(
#    primeiro_nome =
#    nome_do_meio =
#    ultimo_nome = 
#    data_de_nascimento = #datetime
#    CPF= 
#)


#projeto = Projeto(
#        titulo= #string
#        #lista_autores=
#        descricao= #string
#        #lista_orientadores=
#        #lista_coorientadores
#        #lista_colaboradores
#    )

entrust = Projeto(
        titulo= "ENTRUST: SOLUÇÃO E APRESENTAÇÃO GRÁFICA DE FUNÇÕES",
        #lista_autores=,
        descricao= "A Matemática é uma das disciplinas que mais apresenta dificuldades durante os anos escolares. Tais dificuldades podem ser evidenciadas na resolução de problemas matemáticos ligados ao estudo de equações. Visando melhorar o ensino da Matemática, este trabalho visa desenvolver uma aplicação que represente a solução e a visualização gráfica de funções matemáticas de primeiro ao quarto grau. Para o desenvolvimento utilizou-se por base sistemas já existentes, alocando características distinta dos mesmos em uma única aplicação, todavia limitando-se ao objetivo proposto. Por fim, fornecendo uma aplicação web que possa ser utilizada como ferramenta de apoio educacional."
        #lista_orientadores=
        #lista_coorientadores
        #lista_colaboradores
    )
