from flask import Flask, jsonify, request

app = Flask(__name__)

postagens = [
    {
        'titulo': 'Minha Familia',
        'autor': 'Thiago Carvalhoo Rodrigues'

    },

    {
        'titulo': 'Surf na indornésia',
        'autor': 'Thiago Carvalhop Rodrigues'

    }

    {

        'titulo': 'Frente a frente com GOD',
        'autor': 'Thiago Carvalhop Rodrigues'

    }

]
@app.route('/postagens',methods=['GET'])
def obter_todas_postagens():
    return jsonify(postagens)

@app.route('/postagens/<int:postagem_id>',methods=['GET'])
def obter_postagens_por_id(postagem_id):
    return jsonify(postagens[postagem_id])

@app.route('/postagens',methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)
    return jsonify({'mensagem': 'recurso criando com sucesso'}),200

@app.route('/postagens/<int:postagem_id>',methods=['PUT'])
def atualizar_postagem(postagem_id):
    resultado = request.get_json()
    postagens[postagem_id].update(resultado)
    return jsonify(postagens[postagem_id]),200

@app.route('/postagens/<int:postagem_id>', methods=['DELETE'])
def excluir_postagem(postagem_id):

    del postagens[postagem_id]
    return jsonify({"mensagem":" A postagem foi excluiída com sucesso"})


if __name__ =='__main__':
    app.run(port=5000, host='localhost',debug=True)