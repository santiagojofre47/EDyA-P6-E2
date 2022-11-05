from claseNodo import Nodo

class ColaEncadenada:
    __ul = None
    __pr = None
    __cant = None

    def __init__(self):
        self.__cant = 0
    
    def vacia(self):
        resultado = None
        if self.__cant == 0:
            resultado = True
        else:
            resultado = False
        return resultado
    
    def insertar(self, x):
        nodo = Nodo()
        nodo.cargar(x)

        if self.__ul == None:
            self.__pr = nodo
        else:
            self.__ul.setSiguiente(nodo)
        self.__ul = nodo
        self.__cant+=1

        return x
    
    def suprimir(self):
        valor = None
        if self.vacia():
            print('ERROR: Cola vacia!')
            valor = 0
        else:
         
            valor = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            if self.__pr == None:
                self.__ul = None
            self.__cant-=1
        return valor
    
    def recorrer(self):
        aux = self.__pr
        while aux != None:
            print('Elemento: {}' .format(aux.getDato()))
            aux = aux.getSiguiente()