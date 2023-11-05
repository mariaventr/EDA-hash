import random
import numpy as np

class Nodo:
    def __init__(self, clave, valor):
        self.__clave = clave
        self.__valor = valor
        self.__siguiente = None

    def get_clave(self):
        return self.__clave

    def get_valor(self):
        return self.__valor

    def get_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

class TablaHashConEncadenamiento:
    def __init__(self, M):
        self.__M = M
        self.__tabla = np.empty(M, dtype=object)

    def __hash(self, clave):
        k_str = str(clave)  # Convertir la clave numérica a una cadena
        longitud = len(k_str)
        parte = longitud // 2
        suma = 0
        for i in range(0, longitud, parte):
            suma += int(k_str[i:i+parte])
        return suma % self.__M

    def insertar(self, clave, valor):
        direccion = self.__hash(clave)
        nuevo_nodo = Nodo(clave, valor)
        if self.__tabla[direccion] is None:
            self.__tabla[direccion] = nuevo_nodo
        else:
            actual = self.__tabla[direccion]
            while actual.get_siguiente():
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo_nodo) 

    def longitud_listas(self):
        longitudes = np.zeros(self.__M, dtype=int)
        for i in range(self.__M):
            actual = self.__tabla[i]
            while actual:
                longitudes[i] += 1
                actual = actual.get_siguiente()
        return longitudes

    def contar_listas_por_exceso_defecto(self):
        longitudes = self.longitud_listas()
        promedio = sum(longitudes) / len(longitudes)
        contador_exceso = 0  # Para contar las listas por exceso
        contador_defecto = 0  # Para contar las listas por defecto

        for longitud in longitudes:
            diferencia = abs(longitud - promedio)
            if diferencia <= 3:
                if longitud > promedio:
                    contador_exceso += 1  # Lista por exceso
                elif longitud < promedio:
                    contador_defecto += 1  # Lista por defecto

        return contador_exceso, contador_defecto
    
    def buscar(self, clave):
        direccion = self.__hash(clave)
        actual = self.__tabla[direccion]

        while actual:
            if actual.get_clave() == clave:
                return True  # Clave encontrada
            actual = actual.get_siguiente()

        return False  # Clave no encontrada
    

    def mostrar_tabla(self):
        for i in range(self.__M):
            actual = self.__tabla[i]
            print(f"Clave - Valor en Índice {i}:")
            while actual:
                print(f"Clave: {actual.get_clave()}, Valor: {actual.get_valor()}")
                actual = actual.get_siguiente()


# Crear una tabla hash con 1000 claves y M = 50 (por ejemplo)
M = 5
tabla_hash = TablaHashConEncadenamiento(M)

# Generar 1000 claves aleatorias y almacenarlas en la tabla hash
#claves = [random.randint(1, 10000) for _ in range(10)]
claves = [528, 1214, 1637, 8750, 251, 7208, 2087, 698, 9643, 8146]
for clave in claves:
    valor = "0"
    tabla_hash.insertar(clave, valor)

# Obtener la longitud de cada lista
longitudes = tabla_hash.longitud_listas()
print("Longitud de cada lista:", longitudes)

# Contar listas que varían en hasta 3 unidades respecto al promedio
exceso, defecto = tabla_hash.contar_listas_por_exceso_defecto()
print("Listas por exceso:", exceso)
print("Listas por defecto:", defecto)

clave_buscada = 9643
encontrada = tabla_hash.buscar(clave_buscada)

if encontrada:
    print(f"Clave {clave_buscada} encontrada en la tabla hash.")
else:
    print(f"Clave {clave_buscada} no encontrada en la tabla hash.")

# Después de insertar todas las claves y valores en la tabla hash, puedes llamar a la función para mostrarlos:
tabla_hash.mostrar_tabla()

