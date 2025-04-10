#Ejercicio 6

import numpy as np

# Crear un arreglo de 10x10x10 lleno de ceros
arreglo = np.zeros((10, 10, 10), dtype=int)

#Definimos los numero primos entre 0 y 9
primos = [2, 3, 5, 7]

#print(np.arange(10))
#Definir condicion de numero impar
impar = np.arange(10) % 2 == 1
#Definir condicion de numero par
par = np.arange(10) % 2 == 0
#Buscar si numero esta dentro de lista de primos
primo = np.isin(np.arange(10), primos)

#Aplicacion de mascaras por indice de arreglo
mascara = impar[:, None, None] & par[None, :, None] & primo[None, None, :]

#Asignar 1 donde la máscara sea True, es deciir, la condicion se cumplio
arreglo[mascara] = 1

#Verificar que funcione imprimiendo algunos elementos
#Elementos que imprimira la prueba
N = 5
#Que se cumpla la condicion de == 1
indices = np.argwhere(arreglo == 1)[:N] 

print(f"Los primeros {N} índices donde el valor es 1:")
for idx in indices:
    #Que el resultado sea de enteros
    print(tuple(map(int, idx))) 