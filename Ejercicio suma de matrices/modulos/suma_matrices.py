
matriz_vacia1 = []  
matriz_vacia2 = []  
matriz_vacia3 = []
n = int(input('Elige el tamaño de la matriz: \n'))  

def matriz1():
    print('Matriz 1:')
    
    for i in range(n):
        matriz_vacia1.append([])  # agrega una lista vacía a la matriz
        for j in range(n):
            valor = int(input(f'Ingresa el valor para la posición ({i},{j}): '))  
            matriz_vacia1[i].append(valor)  # agrega el valor ingresado a la matriz en la posición (i,j)

    print('Estas es la matriz 1:')
    for k in range(n):
        print(matriz_vacia1[k])


def matriz2():
    print('Matriz 2:')
    for i in range(n):
        matriz_vacia2.append([])
        for j in range(n):
            valor = int(input(f'Ingresa el valor para la posición ({i},{j}): '))  
            matriz_vacia2[i].append(valor)
    
    print('Esta es la matriz 2:')
    for k in range(n):
        print(matriz_vacia2[k])


def suma(): 
    for i in range(n):
        matriz_vacia3.append([]) 
        for j in range(n):
            matriz3 = matriz_vacia3[i].append(matriz1[i][j] + matriz2[i][j])  
    
    print('La suma de las matrices es:')
    for k in range(n):
        print(matriz3[k])

def suma_completa():
    matriz1()
    matriz2()
    suma()


