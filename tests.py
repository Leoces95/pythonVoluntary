# Expresiones lamnbda en python
from test2 import Persona
import numpy as np
#print(np.__version__)
class Arreglos():    

    def __init__(self) -> None:
        pass
    
    def diccionarios(self):
        sujeto = Persona("Leoces", "Martinez", 34, 173)
        diccionario1 = {"nombre": sujeto }
        return diccionario1["nombre"]
    def diccionarios2(self):
        dic = {"Alejandro": [22, 1.73], "Jose": [23, 1.72]}
        print(dic)
    def diccionario3(self, id):
        diccio3 = {"1":"Leoces","2":"Yeilis", "3":"David", "4":"Ufenil"}
        if str(id) in diccio3:
            print('Encontrado' + diccio3.get(id))
        else:
            print('No encontrado')

    def sumar(self, a, b) :
        return (a+b)

llamado = Arreglos()
#llamado.diccionarios2()
llamado.diccionario3(2)
# ejemplos de arreglos
# listas
lista = [1,2,4,5]
tuplas = (1,2,3,4,5)
vector = np.array([1,2,3,4,5])
matriz = np.array([[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]])
#print(lista, tuplas, vector, matriz)
sumador = 0
for fila in matriz:
    for valor in fila:  
        sumador+=valor
#print(sumador)
#print(valor)


