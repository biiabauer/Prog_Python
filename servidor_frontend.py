from config import *
from modelo import Livro

@app.route("/")
def inicio():
    return 'Sistema de cadastro de livros: front-end. '+\
        '<a href="/listar_livros">Operação listar</a>'

@app.route("/listar_livros")
def listar_livros():
    # obter os livros do back-end
    resultado_requisicao = requests.get('http://localhost:5000/listar_livros')
    # dados json podem ser carregados em dicionários do python
    json_livros = resultado_requisicao.json() 
    # inicializar uma lista do python
    livros_em_python = []
    # percorrer os livros em json
    for l in json_livros:
        # criar um livro passando as informações do dicionário
        li = Livro(**l)
        # adicionar o livro convertida na lista de livros
        livros_em_python.append(li)
    
    # fornecer a lista de livros para a página exibir os livros
    return render_template("listar_livros.html", listagem = livros_em_python)

app.run(debug=True, port=4999)