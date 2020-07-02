from config import *
from modelo import Livro

@app.route("/")
def inicio():
    return 'Sistema de cadastro de livros. '+\
        '<a href="/listar_livros">Operação listar</a>'

@app.route("/listar_livros")
def listar_pessoas():
    # obter os livros do cadastro
    livros = db.session.query(Livro).all()
    # aplicar o método json que a classe Livro possui a cada elemento da lista
    livros_em_json = [ x.json() for x in livros ]
    # fornecer a lista de livros em formato json
    return jsonify(livros_em_json)

app.run(debug=True)