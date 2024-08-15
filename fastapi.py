from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definir un modelo de datos usando Pydantic
class Usuario(BaseModel):
    nombre: str
    edad: int

# Endpoint para obtener un saludo
@app.get("/")
def read_root():
    return {"mensaje": "Hola, Mundo"}

# Endpoint para obtener información de un usuario
@app.get("/usuarios/{usuario_id}")
def read_usuario(usuario_id: int):
    return {"usuario_id": usuario_id}

# Endpoint para crear un nuevo usuario
@app.post("/usuarios/")
def create_usuario(usuario: Usuario):
    return {"usuario": usuario}

# Ejecutar el servidor
# uvicorn main:app --reload
