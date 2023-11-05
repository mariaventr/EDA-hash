def funcion_division(k, M):
    return k % M

def funcion_extraccion(k, M, n):
    return int(str(k)[-n:]) % M

def funcion_plegado(k, M, num_partes):
    k_str = str(k)  # Convertir la clave numérica a una cadena
    longitud = len(k_str)
    parte = longitud // num_partes
    suma = 0
    for i in range(0, longitud, parte):
        suma += int(k_str[i:i+parte])
    return suma % M

def funcion_cuadrado_medio(k, M, num_dígitos):
    cuadrado = k * k
    centro = (len(str(cuadrado)) - num_dígitos) // 2
    resultado = int(str(cuadrado)[centro:centro+num_dígitos])
    return resultado % M

def funcion_alfanumerica(k, M):
    suma_ascii = sum(ord(c) for c in k)
    return suma_ascii % M


'''# Definir una clave y el tamaño de la tabla
clave = 20810
M = 33  # Tamaño de la tabla
n = 2 # Número de dígitos a extraer
ubicacion = funcion_extraccion(clave, M, n)
# Imprimir el resultado
print(f"Clave: {clave}, Ubicación en la tabla hash: {ubicacion}")'''

'''clave =20810
M = 33  # Tamaño de la tabla
n = 2 # Número de dígitos a extraer
ubicacion = funcion_plegado(clave, M, n)
# Imprimir el resultado
print(f"Clave: {clave}, Ubicación en la tabla hash: {ubicacion}")'''

'''clave =20810
M = 33  # Tamaño de la tabla
n = 3 # Número de dígitos a extraer
ubicacion = funcion_cuadrado_medio(clave, M, n)
# Imprimir el resultado
print(f"Clave: {clave}, Ubicación en la tabla hash: {ubicacion}")'''

# Ejemplo de uso
clave_1 = "Hello123"  # Una clave alfanumérica
M = 10  # Tamaño de la tabla hash

ubicacion = funcion_alfanumerica(clave_1, M)
print(f"La ubicación en la tabla hash para la clave '{clave_1}' es {ubicacion}")




