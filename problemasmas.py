#Matias Valdes Jose Ignacio
#Caamal Pat Jesus Fernando
#Velazquez Chi Alex Jhovani




#1
def eliminar_elemento(arreglo, elemento):
    nuevo_arreglo = [] 
    for x in arreglo:
        if x != elemento:
            nuevo_arreglo.append(x)
    return nuevo_arreglo

#Ejemplo
arreglo = [1, 2, 3, 4, 5]
elemento_a_eliminar = 3
print("Arreglo original:", arreglo)
resultado = eliminar_elemento(arreglo, elemento_a_eliminar)
print("Arreglo sin el elemento:", resultado) 







#2
def agregar_al_final(arreglo, elemento):
    nuevo_arreglo = arreglo + [elemento] 
    return nuevo_arreglo 

#Ejemplo
arreglo = [1, 2, 3]
nuevo_elemento = 4
print("Arreglo original:", arreglo)
resultado = agregar_al_final(arreglo, nuevo_elemento)
print("Arreglo con el nuevo elemento:", resultado)  






#3
def buscar_elemento(arreglo, elemento):
    for i in range(len(arreglo)):
        if arreglo[i] == elemento: 
            return i 
    return -1 

#Ejemplo
arreglo = [10, 20, 30, 40]
elemento_a_buscar = 30
print("Arreglo:", arreglo)
resultado = buscar_elemento(arreglo, elemento_a_buscar)
if resultado != -1:
    print(f"Elemento encontrado en la posición: {resultado}")
else:
    print("Elemento no encontrado.") 








#4
def buscar_y_agregar(arreglo, elemento):
    for i in range(len(arreglo)):
        if arreglo[i] == elemento:  
            return i  

    arreglo = arreglo + [elemento]  
    return len(arreglo) - 1  

#Ejemplo
arreglo = [1, 2, 3]
elemento_a_buscar = 4
print("Arreglo inicial:", arreglo)
resultado = buscar_y_agregar(arreglo, elemento_a_buscar)
print("Arreglo final:", arreglo)
print(f"Posición del elemento (nuevo o existente): {resultado}") 











#5
def crear_matriz(m, n, valor):
    matriz = []  
    for i in range(m):  
        fila = []  
        for j in range(n): 
            fila.append(valor)
        matriz.append(fila)  
    return matriz

#Ejemplo
filas = 3
columnas = 4
valor_inicial = 0
matriz = crear_matriz(filas, columnas, valor_inicial)
print("Matriz creada:")
for fila in matriz:
    print(fila)








#6
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_transpuesta = []  
    for j in range(columnas):  
        nueva_fila = []  
        for i in range(filas):  
            nueva_fila.append(matriz[i][j])  
        matriz_transpuesta.append(nueva_fila) 
    return matriz_transpuesta

#Ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz_transpuesta = transponer_matriz(matriz)
print("Matriz original:")
for fila in matriz:
    print(fila)

print("Matriz transpuesta:")
for fila in matriz_transpuesta:
    print(fila)














#7
def suma_matriz(matriz):
    suma = 0
    for fila in matriz: 
        for elemento in fila: 
            suma += elemento  
    return suma

#Ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
resultado = suma_matriz(matriz)
print("Suma de matrices:", resultado) 












#8
def insertar_en_orden(matriz, elemento):
    for fila in matriz: 
        if elemento <= fila[-1]: 
            for i in range(len(fila)):
                if elemento <= fila[i]:  
                    fila.insert(i, elemento)  
                    return matriz
    matriz[-1].append(elemento)
    return matriz

#Ejemplo
matriz = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
elemento = 6
print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_modificada = insertar_en_orden(matriz, elemento)
print("Matriz después de insertar el elemento:")
for fila in matriz_modificada:
    print(fila)











#9
def buscar_en_matriz_ordenada(matriz, elemento):
    for i, fila in enumerate(matriz):  
        if elemento in fila: 
            j = fila.index(elemento)  
            return (i, j)  
    return -1  

#Ejemplo
matriz = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
elemento_a_buscar = 9
print("Matriz:")
for fila in matriz:
    print(fila)

posicion = buscar_en_matriz_ordenada(matriz, elemento_a_buscar)
if posicion != -1:
    print(f"Elemento encontrado en la posición: {posicion}")  
else:
    print("Elemento no encontrado.")












#10
def ordenar_matriz_burbuja(matriz):
    elementos = [elemento for fila in matriz for elemento in fila]

    n = len(elementos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if elementos[j] > elementos[j + 1]:
                elementos[j], elementos[j + 1] = elementos[j + 1], elementos[j]

    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_ordenada = [[0] * columnas for _ in range(filas)]  
    index = 0  
    for i in range(filas):
        for j in range(columnas):
            matriz_ordenada[i][j] = elementos[index]  
            index += 1

    return matriz_ordenada

#Ejemplo
matriz = [
    [9, 7, 3],
    [6, 5, 2],
    [8, 4, 1]
]
print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_ordenada = ordenar_matriz_burbuja(matriz)
print("Matriz ordenada:")
for fila in matriz_ordenada:
    print(fila)

