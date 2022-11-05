import random
from claseGrafo import GrafoSecuencial


if __name__ == '__main__':
    obj = GrafoSecuencial(5)
    obj.crearArista(1, 2)
    obj.crearArista(1, 3)
    obj.crearArista(5, 2)
    obj.crearArista(2, 5)
    obj.crearArista(2, 4)
    obj.crearArista(4, 3)
    '''for i in range(20):
        x = random.randint(1,obj.getCantidadVertices())
        y = random.randint(1,obj.getCantidadVertices())
        obj.crearArista(x,y)'''
    if obj.Conexo():
        print('Grafo conexo')
    else:
        print('Grafo no conexo')
    if obj.Ciclico(1):
        print('s')    
 