#Ejercicio 3

import numpy as np

#Puntajes aleatorios entre 0 y 100 para 10 parejas
generator = np.random.default_rng(1010)
data = np.round (generator.uniform (low=0, high=101,size=10))
puntajes = data
#puntajes = np.random.randint(0, 101, size=10)  
print("Los puntajes de amor de los 10 participantes fueron: ", puntajes)

#Funcion para determinar el puntaje de amor, similares hacen match
def dif_puntajes_amor(puntajes):
    #Dimension de matriz
    n = len(puntajes)
    #Broadcast para detereminar diferencias
    #Generar matriz convirtiendo en columna ("hombres") y fila ("mujeres") los puntajes
    #Se realiza una resta del valor fila 1 (mujer 1) menos columna 1 (hombre 1)
    diferencias = np.abs(puntajes.reshape(n,1) - puntajes.reshape(1,n))
    return diferencias
    
Arreglo_match = dif_puntajes_amor(puntajes)
print("El arreglo 2D de la diferencia de los puntajes de amor es: ", Arreglo_match)