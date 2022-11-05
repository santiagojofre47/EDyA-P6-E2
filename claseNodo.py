class Nodo:
    __elemento = None
    __sig = None

    def cargar(self, x):
        assert isinstance(x, int)
        self.__elemento = x
        self.__sig = None

    def setSiguiente(self, sig):
        self.__sig = sig

    def getDato(self):
        return self.__elemento

    def getSiguiente(self):
        return self.__sig    