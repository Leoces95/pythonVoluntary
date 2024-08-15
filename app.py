from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta raíz
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenido a la API"})

# Ruta para obtener un usuario por ID
@app.route('/usuario/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    usuarios = {1: "Juan", 2: "Ana", 3: "Pedro", 4: "Leoces"}
    usuario = usuarios.get(usuario_id, "No encontrado")
    return jsonify({"usuario_id": usuario_id, "nombre": usuario})

# Ruta para crear un nuevo usuario
@app.route('/usuario', methods=['POST'])
def create_usuario():
    data = request.json
    nombre = data.get("nombre", "Nombre no proporcionado")
    return jsonify({"mensaje": f"Usuario {nombre} creado"}), 201

@app.route('/usuario/<int:usuario_id>', methods=['DELETE'])
def eliminar(usuario_id):
    #usuarios = get_usuario(user_id)
    usuarios = {"1": "Leoces", "2":"Yeilis","3":"Emily", "4": "Tania"}
    
    if(usuario_id in usuarios):
        return jsonify({"mensaje": "USUARIO ELIMINADO: " + {usuarios.get(str("usuario_id"))}})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"})
if __name__ == '__main__':
    app.run(debug=True)
    
