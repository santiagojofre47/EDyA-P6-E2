import numpy as np 
from claseColaEncadenada import ColaEncadenada

class GrafoSecuencial:
    __matrizAdyacencia = None
    __cantVertices =  None

    def __init__(self, cant_vertices = 3):
        self.__cantVertices = cant_vertices
        self.__matrizAdyacencia = np.zeros((self.__cantVertices,self.__cantVertices),dtype = int)
    
    def crearArista(self, v1, v2):
        if (v1 <= self.__cantVertices and v2 <= self.__cantVertices) and (v1 >= 1 and v2 >= 1):
            self.__matrizAdyacencia[v1-1][v2-1] = 1
           
        else:
            print('ERROR: Vertices no validos')
    
    def Adyacentes(self, v):
        list = []
        if v < self.__cantVertices and v>= 0:
            for j in range(self.__cantVertices):
                if self.__matrizAdyacencia[v][j] == 1:
                    list.append(j) 
        return list
    
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
        predecesores = np.zeros(self.__cantVertices,dtype = int)
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
                    predecesores[ady] = nodo
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
        P = self.__matrizAdyacencia
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

    def mostrarMatriz(self):
        print(self.__matrizAdyacencia)
        
    def getCantidadVertices(self):
        return self.__cantVertices