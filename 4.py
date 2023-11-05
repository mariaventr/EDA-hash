import random
import numpy as np

class Bucket:
    def __init__(self, b):
        self.data = np.empty(b, dtype=object)  # Usar un arreglo NumPy para almacenar las claves

class TablaHashConBuckets:
    def __init__(self, M, b, digitos_a_extraer):
        self.M = M  # Tamaño de la tabla
        self.b = b  # Tamaño de cada Bucket
        self.digitos_a_extraer = digitos_a_extraer  # Cantidad de dígitos a extraer
        self.area_primaria = np.array([Bucket(b) for _ in range(M)], dtype=object)
        self.area_overflow = np.array([Bucket(b) for _ in range(M // 5)], dtype=object)  # Área de Overflow (20% de M)
        self.buckets_desbordados = 0
        self.buckets_subocupados = 0

    def hash(self, clave):
        # Extraer los dígitos correspondientes
        digitos = int(str(clave)[-self.digitos_a_extraer:])
        return digitos % self.M

    def insertar(self, clave, valor):
        bucket_index = self.hash(clave)
        bucket = self.area_primaria[bucket_index]

        # Verificar si el Bucket está lleno
        if all(bucket.data):
            # El Bucket está lleno, se usa el área de overflow
            bucket_index_overflow = bucket_index % len(self.area_overflow)
            bucket_overflow = self.area_overflow[bucket_index_overflow]

            if not all(bucket_overflow.data):
                # El Bucket de Overflow no está lleno, insertar la clave
                for i in range(self.b):
                    if bucket_overflow.data[i] is None:
                        bucket_overflow.data[i] = (clave, valor)
                        return
        else:
            # El Bucket aún tiene espacio, insertar la clave
            for i in range(self.b):
                if bucket.data[i] is None:
                    bucket.data[i] = (clave, valor)
                    return

    def contar_buckets_subocupados(self):
        for bucket in self.area_primaria:
            ocupados = sum(1 for clave in bucket.data if clave is not None)
            if ocupados < self.b:
                self.buckets_subocupados += 1

    def contar_buckets_desbordados(self):
        # Contar buckets desbordados en el área primaria
        buckets_primaria = [bucket for bucket in self.area_primaria if all(bucket.data)]
        # Contar buckets desbordados en el área de overflow
        buckets_overflow = [bucket for bucket in self.area_overflow if all(bucket.data)]
        return {
            "Buckets Desbordados en Área Primaria": len(buckets_primaria),
            "Buckets Desbordados en Área de Overflow": len(buckets_overflow)
        }

    def obtener_info_colisiones(self):
        return {
            "Buckets Desbordados": self.contar_buckets_desbordados(),
            "Buckets Subocupados": self.buckets_subocupados
        }
    
    def mostrar_tabla(self):
        print("Área Primaria:")
        for i, bucket in enumerate(self.area_primaria):
            print(f"Bucket {i}:")
            for j, elemento in enumerate(bucket.data):
                if elemento is not None:
                    clave, valor = elemento
                    print(f"  Clave: {clave}, Valor: {valor}")
                else:
                    print(f"  Espacio {j}: Vacío")

        print("\nÁrea de Overflow:")
        for i, bucket in enumerate(self.area_overflow):
            print(f"Bucket de Overflow {i}:")
            for j, elemento in enumerate(bucket.data):
                if elemento is not None:
                    clave, valor = elemento
                    print(f"  Clave: {clave}, Valor: {valor}")
                else:
                    print(f"  Espacio {j}: Vacío")

    def buscar(self, clave):
        bucket_index = self.hash(clave)
        bucket = self.area_primaria[bucket_index]
        # Buscar la clave en el Bucket primario
        for i in range(self.b):
            print(bucket.data[i][0])
            if bucket.data[i] and bucket.data[i][0] == clave:
                return bucket.data[i][1]  # Devolver el valor asociado a la clave
        # Buscar la clave en el Área de Overflow
        bucket_index_overflow = bucket_index % len(self.area_overflow)
        bucket_overflow = self.area_overflow[bucket_index_overflow]
        for i in range(self.b):
            if bucket_overflow.data[i] and bucket_overflow.data[i][0] == clave:
                return bucket_overflow.data[i][1]  # Devolver el valor asociado a la clave
        # La clave no se encontró
        return None



N = 10  # Cantidad de claves numéricas
M = 5 # Tamaño de la tabla
b = 2  # Tamaño de cada Bucket

tabla_hash = TablaHashConBuckets(M, b, 3)

# Generar claves numéricas aleatorias e insertarlas en la tabla hash
#claves = [random.randint(1, 10000) for _ in range(N)]
#claves = [528, 1214, 1637, 8750, 251, 7208, 2087, 698, 9643, 8146]
claves = [66, 467, 566, 735, 285, 87]
print(claves)
for clave in claves:
    valor="0"
    tabla_hash.insertar(clave, valor)

# Contar Buckets subocupados
tabla_hash.contar_buckets_subocupados()

# Obtener información sobre las colisiones
info_colisiones = tabla_hash.obtener_info_colisiones()

print("Información de Colisiones:")
print(info_colisiones)

tabla_hash.mostrar_tabla()

clave_buscada = 66
valor_encontrado = tabla_hash.buscar(clave_buscada)

if valor_encontrado is not None:
    print(f"Clave {clave_buscada} encontrada, valor: {valor_encontrado}")
else:
    print(f"Clave {clave_buscada} no encontrada")
