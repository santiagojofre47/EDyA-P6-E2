import numpy as np
from claseListaPosicion import ListaEncadenada
from claseColaEncadenada import ColaEncadenada

class GrafoEnlazado:
    __arreglo = None
    __cantVertices = None

    def __init__(self,cantidad_vertices):
        self.__arreglo = np.empty(cantidad_vertices,dtype =ListaEncadenada)
        self.__cantVertices = cantidad_vertices

        for i in range(self.__cantVertices):
            lista_adyacencia = ListaEncadenada()
            self.__arreglo[i] = lista_adyacencia
    
    
    def crearArista(self, v1, v2):
        if (v1 <= self.__cantVertices and v2 <= self.__cantVertices) and (v1 >= 1 and v2 >= 1):
            p = self.__arreglo[v1-1].getTamanio()
            self.__arreglo[v1-1].insertar(v2-1,p)

        else:
            print('ERROR: Vertices no validos')
    
    def Adyacentes(self, vertice):
        lista = None
        if vertice >= 0 and vertice < self.__cantVertices:
            lista = self.__arreglo[vertice].getVertices()

        else:
            print('Error: vertice no valido')
        return lista
    
    def mostrar(self):
        for i in range(self.__cantVertices):
            print('Vertice: {} adyacentes: {}'.format(i+1,self.__arreglo[i].mostrar()))
    
   #Metodo recorrido en profundidad
    def REP(self, actual,arreglo = None, recorrido = None, iniciar = False):
        if not iniciar:
            if actual-1 >=0  and actual-1 < self.__cantVertices:
                arreglo = np.zeros(self.__cantVertices,dtype = int)
                recorrido = []
                recorrido = self.REP(actual = actual-1 , arreglo = arreglo,recorrido = recorrido, iniciar = True)
            else:
                print('ERROR: vertice  origen no valido')
                return None
        else:
            recorrido.append(actual+1)
            arreglo[actual] = 1
            adyacentes = self.Adyacentes(actual)
            for adyacente in adyacentes:
                if arreglo[adyacente] == 0:
                   recorrido =  self.REP(adyacente,arreglo = arreglo,recorrido = recorrido, iniciar = True)
         
        return recorrido

    
    #Metodo recorrido en anchura
    def REA(self, origen):
        arreglo = np.empty(self.__cantVertices,dtype = int)
        cola = ColaEncadenada()
        recorrido = []
        for i in range(self.__cantVertices):
            arreglo[i] = 99999
        arreglo[origen-1] = 0#Marcamos el vertice de origen
        cola.insertar(origen-1)
        while not cola.vacia():
            nodo = cola.suprimir()
            recorrido.append(nodo+1)
            for ady in self.Adyacentes(nodo):
                if arreglo[ady] == 99999:
                    arreglo[ady] = 0
                    cola.insertar(ady)
        return recorrido
    
    #Metodo para obtener los predecesores de todos los nodos des utilizando el recorrido en anchura a partir de un nodo de origen
    def getPredecesoresREA(self, origen):
        arreglo = np.empty(self.__cantVertices,dtype = int)
        cola = ColaEncadenada()
        predecesores = np.zeros(self.__cantVertices,dtype = int)
        for i in range(self.__cantVertices):
            arreglo[i] = 99999
        arreglo[origen] = 0#Marcamos el vertice de origen
        cola.insertar(origen)
        while not cola.vacia():
            nodo = cola.suprimir()
            for ady in self.Adyacentes(nodo):
                if arreglo[ady] == 99999:
                    arreglo[ady] = 0
                    predecesores[ady] = nodo+1
                    cola.insertar(ady)
        return predecesores

    #Metodo para obtener los predecesores de todos los nodos des utilizando el recorrido en profundidad a partir de un nodo de origen
    def getPredecesoresREP(self, actual,predecesores = None,arreglo = None, recorrido = None, iniciar = False):
        if not iniciar:
            if actual-1 >=0  and actual-1 < self.__cantVertices:
                arreglo = np.zeros(self.__cantVertices,dtype = int)
                predecesores = np.zeros(self.__cantVertices,dtype = int)
                predecesores = self.getPredecesoresREP(actual = actual-1 , arreglo = arreglo,predecesores = predecesores, iniciar = True)
            else:
                print('ERROR: vertice  origen no valido')
                return None
        else:
            arreglo[actual] = 1
            adyacentes = self.Adyacentes(actual)
            for adyacente in adyacentes:
                if arreglo[adyacente] == 0:
                   predecesores[adyacente] = actual+1
                   predecesores =  self.getPredecesoresREP(adyacente ,arreglo = arreglo,predecesores = predecesores, iniciar = True)
        return predecesores

    def camino_minimo(self,origen,destino):
        predecesores = self.getPredecesoresREA(origen-1)
        camino = []
        actual = destino
        while  actual != 0:
            camino.append(actual)
            actual = predecesores[actual-1]
        if origen < destino:
            camino.sort(reverse=False)
        else:
            camino.sort(reverse=True)
        return camino
    
    def camino(self,origen,destino):
        predecesores = self.getPredecesoresREP(origen)
        actual = destino
        camino = []
        while actual != 0:
            camino.append(actual)
      
            actual = predecesores[actual-1]
       
        if origen < destino:
            camino.sort(reverse=False)
        else:
            camino.sort(reverse=True)
        return camino
    
    def Warshall(self):
        P = np.zeros((self.__cantVertices,self.__cantVertices),dtype=int)

        for i in range(self.__cantVertices):
            for j in range(self.__cantVertices):
                if j in self.Adyacentes(i):
                    P[i][j] = 1
        
        for k in range(self.__cantVertices):
            for i in range(self.__cantVertices):
                for j in range(self.__cantVertices):
                    if P[i][j] == 1 or (P[i][k]*P[k][j]) == 1:
                        P[i][j] = 1
                    else:
                        P[i][j] = 0
        return P
 
    def Conexo(self):
        matriz_caminos = self.Warshall()
        band = True
        i = 0
        while i < self.__cantVertices and  band:
            j = 0
            while j < self.__cantVertices:
                if matriz_caminos[i][j] == 0:
                    band = False
                j+=1
            i+=1
        return band
    
    def Ciclico(self, actual, arreglo = None, recorrido = None, ciclico = None, iniciar = False):
        if not iniciar:
            if actual-1 >=0  and actual-1 < self.__cantVertices:
                arreglo = np.zeros(self.__cantVertices,dtype = int)
                recorrido = []
                ciclico = self.Ciclico(actual = actual-1 , arreglo = arreglo, recorrido = recorrido,ciclico = ciclico, iniciar = True)
            else:
                print('ERROR: vertice  origen no valido')
                return None
        else:
            if ciclico == True:
                return ciclico
            recorrido.append(actual+1)
            arreglo[actual] = 1
            adyacentes = self.Adyacentes(actual)
            for adyacente in adyacentes:
                if arreglo[adyacente] == 0:
                   ciclico =  self.Ciclico(adyacente,arreglo = arreglo,recorrido = recorrido,ciclico = ciclico, iniciar = True)
                elif len(recorrido) >= 3:
                    ciclico = True         
        return ciclico

    
if __name__ == '__main__':
    obj = GrafoEnlazado(6)
    obj.crearArista(1, 2)
    obj.crearArista(1, 3)
    obj.crearArista(2, 4)
    obj.crearArista(2, 5)
    obj.crearArista(5, 4)
    obj.mostrar()
    if not obj.Conexo():
        print('Grafo no conexo!')
   



     
    
    
    
