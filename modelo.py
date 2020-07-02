from config import *

class Livro(db.Model):
    # atributos da pessoa
    nome = db.Column(db.String(254), primary_key=True)
    autor = db.Column(db.String(254))
    ano = db.Column(db.String(254))

    # método para expressar o livro em forma de texto
    def __str__(self):
        return str(self.nome)+" de "+ self.autor + ", " + self.ano 
    # expressao da classe no formato json
    def json(self):
        return {
            "nome": self.nome,
            "autor": self.autor,
            "ano": self.ano,
        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Livro
    l1 = Livro(nome = "A noiva fantasma", autor = "Yangsze Choo", 
        ano = "2015")
    l2 = Livro(nome = "Névoa", autor = "Kathyn James", 
        ano = "2014")        
    
    # persistir
    db.session.add(l1)
    db.session.add(l2)
    db.session.commit()
    
    # exibir o livro
    print(l2)

    # exibir a pessoa no format json
    print(l2.json())