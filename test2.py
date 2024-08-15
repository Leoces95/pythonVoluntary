class Persona():
    def __init__(self, nombre: str, apellido: str, edad: int, estatura: float) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estatura = estatura
        pass
    def identificacion(self):
        print (f"Saludos, {self.nombre} {self.apellido} Edad: {self.edad}, Estatura: {self.estatura}")

    def saludo(self):
        print(f"Hola, {self.nombre}")