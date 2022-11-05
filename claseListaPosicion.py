import numpy as np
from claseNodo import Nodo

class ListaEncadenada:
    __cab = None
    __cant = None
    
    def __init__(self):
        self.__cab = None
        self.__cant = 0
    def getTamanio(self):
        return self.__cant
    def vacia(self):
        return (self.__cab == None)

    def insertar(self, elemento, p):
        if p>= 0 and p<= self.__cant:
            i = 0
            aux = self.__cab
            ant = self.__cab
            encontro = False
            if p == 0:#CASO 1: insertar al comienzo de la lista
                nodo = Nodo()
                nodo.cargar(elemento)
                nodo.setSiguiente(self.__cab)
                self.__cab = nodo
                self.__cant+=1
            else: #CASO 2: insertar al medio o al final de la lista
                while not encontro and   aux != None:
                    if i == p:
                        encontro = True
                    else:
                        ant = aux
                        aux = aux.getSiguiente()
                        i+=1
                        
                nodo = Nodo()
                nodo.cargar(elemento)
                ant.setSiguiente(nodo)
                nodo.setSiguiente(aux)
                self.__cant+=1
        else:
                print('ERROR: Posicion no valida')
    
    def suprimir(self, p):
        if p>= 0 and p<=self.__cant:
            enconto = False
          
            i = 0
            if p-1 == 0:#CASO 1: Se quiere eliminar el primer nodo de la lista
                self.__cab = self.__cab.getSiguiente()
            else:
                aux = self.__cab
                ant = aux
                while aux != None and not enconto: #CASO 2: Se quiere eliminar un nodo intermedio o el ultimo nodo de la lista
                    if i == p-1:
                        enconto = True
                    else:
                        i+=1
                        ant = aux
                        aux = aux.getSiguiente()
                ant.setSiguiente(aux.getSiguiente())
                self.__cant-=1
        else:
            print('ERROR: Posicion no valida!')
            
    
   
    def recuperar(self, p):
        val = None
        if not self.vacia():
            i = 0
            if p -1 >= 0 and p -1 <= self.__cant-1:
                encontro = False
                aux = self.__cab
                while not encontro and aux != None:
                    if i == p-1:
                        encontro = True
                    else:
                        aux= self.siguiente(i)
                        i+=1
                val = aux.getDato()
        return val

    def buscar(self, elemento):
        val = None
        if not self.vacia():
            encontro = False
            aux = self.__cab
            i = 0
            while not encontro and aux != None:
                if self.recuperar(i) == elemento:
                    encontro = True
                    val = i
                else:
                    i+=1
                    aux = self.siguiente(i)
            if not encontro:
                print('ERROR: elemento no encontrado!')
        else:
            print('ERROR: Lista vacia!')
        return val
    
    def siguiente(self, p):
        val = None
        if not self.vacia():
            if p >= 0 and p < self.__cant-1:
                aux = self.__cab
                i = 0
                encontro = False
                while not encontro and aux != None:
                    if i == p:
                        encontro = True
                    else:
                        i+=1
                        aux = aux.getSiguiente()
                val = aux.getSiguiente()

        return val
    
    def anterior(self,p):
        val = None
        if not self.vacia():
            if p > 1 and p <= self.__cant:
                aux = self.__cab
                ant = aux
                i = 0
                encontro = False
                while not encontro and aux != None:
                    if i == p-1:
                        encontro = True
                    else:
                        ant = aux
                        aux = self.siguiente(i)
                        i+=1
                val = ant
        return val
    
    def primer_elemento(self):
        val = None
        if not self.vacia():
            val = self.recuperar(1)
        else:
            print('ERROR: lista vacia!')
        return val
    
    def ultimo_elemento(self):
        val = None
        if not self.vacia():
            val = self.recuperar(self.__cant)
        else:
            print('ERROR: lista vacia!')
        return val
    
    def mostrar(self):
        s = ''
        if not self.vacia():
            aux = self.__cab
            while aux != None:
                s+=str(aux.getDato())+'->'
                aux = aux.getSiguiente()
        return s
    
    def getVertices(self):
        aux = self.__cab
        list = []
        while aux != None:
            list.append(aux.getDato())
            aux = aux.getSiguiente()
        return list

