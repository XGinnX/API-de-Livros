# 1. Objetivo - Criar uma API que disponibiliza a consulta, criação, edição, exclusão de livros.
# 2. URL Base - localhost
# 3. Endpoints - 
    # Criar Livros - localhost/livros (POST)
    # Acesso aos livros - localhost/livros (GET)
    # Acesso aos livros por id - localhost/livros/id (GET)
    # Alteração de livros por id - localhost/livros/id (PUT)
    # Deletar livros por id - localhost/livros/id (DELETE)
# 4. Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [{
        'id': 1,
        'titulo': 'Harry Potter e a pedra filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Camara Secreta',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'Harry Potter e as reliquias da morte',
        'autor': 'J.K Howling'
    },
     {
        'id': 4,
        'titulo': 'A Arte da Guerra',
        'autor': 'Sun tzu'
    }, 
    {
        'id': 5,
        'titulo': 'O Príncipe',
        'autor': 'Maquiavel'
    }]


#Consultar todos
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar por Id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id (id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
          livros[indice].update(livro_alterado)
          return jsonify(livros[indice])
#Criar
@app.route('/livros', methods=['POST'])
def adicionar_novo_livro ():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
    
# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
         if livro.get('id') == id:
            del livros[indice]
            
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)