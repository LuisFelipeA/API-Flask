from flask import Flask, request, jsonify #importa flask

app = Flask(__name__) #inicia flask

usuarios = [] #lista de usuarios
id_counter = 1 #contador id

#listar usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

#criar usuario
@app.route('/usuario', methods=['POST'])
def add_usuario():
    global id_counter
    data = request.get_json()
    usuario = {'id': id_counter, 'nome': data['nome'], 'email': data['email']}
    usuarios.append(usuario)
    id_counter += 1
    return jsonify(usuario), 201

#busca usuario por id
@app.route('/usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            return jsonify(usuario)
    return jsonify({'message': 'Usuário não encontrado'}), 404

#edita usuario
@app.route('/usuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            data = request.get_json()
            usuario['nome'] = data['nome']
            usuario['email'] = data['email']
            return jsonify(usuario)
    return jsonify({'message': 'Usuário não encontrado'}), 404

#apaga usuario
@app.route('/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['id'] != id]
    return jsonify({'message': 'Usuário deletado'}), 200

if __name__ == '__main__':
    app.run(debug=True)
