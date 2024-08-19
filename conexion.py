# conexion.py
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from sqlalchemy import text

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializar SQLAlchemy
db = SQLAlchemy()

def init_app(app):
    # Configurar la conexión a SQL Server usando variables de entorno
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_DATABASE')
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    driver = os.getenv('DB_DRIVER')

    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos con la aplicación Flask
    db.init_app(app)

def test_connection():
    try:
        # Ejecutar una consulta simple para verificar la conexión
        with db.engine.connect() as connection:
            result = connection.execute(text('SELECT 1'))
        return {
            'status': 'success',
            'message': 'Conexión exitosa. Consulta ejecutada correctamente.'
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }
