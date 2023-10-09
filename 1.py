#N=cantidad de claves y M tamaño de la tabla
#a=N/M
#0,7=100/M
#M=100/0,7=142
import numpy as np

class tablaHash:
    __tamaño=int
    __arreglo=[]
    def __init__(self, tamaño):
        self.__tamaño=tamaño
        self.__arreglo=np.empty(tamaño, dtype=object)
        
    def hash(self, clave):
        return clave % self.__tamaño
    
    def pruebaSecuencial(self, clave, i):
        return (self.hash(clave)-i) % self.__tamaño # (h(k) – i * p (k) ) mod M 0 <= i <= M-1
    
    def insertar(self, clave, valor):
        i=0
        indice=self.pruebaSecuencial(clave, i)
        while self.__arreglo[indice] is not None:
            i+=1
            indice= self.pruebaSecuencial(clave, i)
        self.__arreglo[indice] = (clave, valor)
            
    def buscar(self, clave):
        i=0
        indice= self.pruebaSecuencial(clave, i)
        print(indice)
        while self.__arreglo[indice] is not None and self.__arreglo[indice][0] != clave:
            i+=1
            indice = self.pruebaSecuencial(clave, i)
        if self.__arreglo[indice] is None:
            return f"la clave no existe"
        return f"longitud {indice}"

    def imprime(self):
        for i, elemento in enumerate(self.__arreglo):
            if elemento is not None:
                clave, valor= elemento
                print(f"indice: {i}, clave: {clave}, valor: {valor}")
            else:
                print(f"indice {i}: vacio")
    
N=5
alfa=0.7
M=int(N//alfa)
hash=tablaHash(M)
claves= [16,8,19,4,5]
for clave in claves:
    hash.insertar(clave, "Valor")

buscar=1
lonSecuencia= hash.buscar(buscar)
print(f"Longitud para la clave: {lonSecuencia}")
