from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta raíz
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenido a la API"})

@app.route('/verTareas', methods=['GET'])
def verTarea():
    return jsonify({"respuesta":"Consulta de tareas desde el backend"})

@app.route('/crearTarea', methods=['OPTIONS', 'POST'])
def crearTarea():
    if request.method == 'OPTIONS':
        return '', 200  # Respuesta de éxito para la solicitud preflight
    
    # Maneja el POST como antes
    data = request.get_json()
    tarea_id = data.get('tarea_id')
    tareas = {1: "Estudiar angular", 2: "Estudiar Hexagonal", 3: "Estudiar Spring Boot", 4: "Estudiar Metodologías"}
    tarea = tareas.get(tarea_id, "No encontrado")
    
    return jsonify({"tarea_id": tarea_id, "nombre": tarea})

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


