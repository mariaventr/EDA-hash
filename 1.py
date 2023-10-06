#N=cantidad de claves y M tamaño de la tabla
#a=N/M
#0,7=100/M
#M=100/0,7=142

class tablaHash:
    __tamaño=int
    __capacidad=int
    __tabla=[]
    def __init__(self, tamaño):
        self.__tamaño=tamaño
        self.__tabla=[None]* self.__tamaño
        
    def hash(self, clave):
        return clave % self.__tamaño
    
    def insertar(self, clave, valor):
        indice=self.hash(clave)
        if self.__tabla[indice] is None:
            self.__tabla[indice] = (clave, valor)
        else:
            while self.__tabla[indice] is not None:
                indice= (indice + 1) % self.__tamaño
            self.__tabla[indice] = (clave, valor)
            
    def buscar(self, clave):
        indice= self.hash(clave)
        pruebas=1
        while self.__tabla[indice] is not None:
            if self.__tabla[indice][0] == clave:
                return pruebas
            indice = (indice + 1)% self.__tamaño
            pruebas+=1
        return pruebas
    

noPrimo= tablaHash(10)
claves= [13,27,42,55,67,78,89,84,101,112]
for clave in claves:
    noPrimo.insertar(clave, "Valor")

buscar=55
lonSecuencia= noPrimo.buscar(buscar)
print(f"Longitud para la clave: {lonSecuencia}")
