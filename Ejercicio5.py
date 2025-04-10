#Ejercicio 5

import numpy as np

locs = np.array ([
[0 ,0 ,0] , #Posicion del primer pez
[1 ,1 ,2] , #Posicion del segundo pez
[0 ,0 ,0] ,
[2 ,1 ,3] ,
[5 ,5 ,4] ,
[5 ,0 ,0] ,
[5 ,0 ,0] ,
[0 ,0 ,0] ,
[2 ,1 ,3] ,
[1 ,3 ,1]
])

generator = np.random.default_rng(1010)
weights = generator.normal(size =10)
print(weights)

#Indexo las posiciones por pez
index = np.arange(locs.shape[0])
#print(index)
locs_con_indices = np.c_[locs, index]
#print(locs_con_indices)

#Agrupar índices de peces por posiciones
repetidos = {}
#Iteramos sobre las posiciones y los indices buscando repeticiones
for i, j, k, idx in locs_con_indices:
    coordenadas = (i, j, k)
    if coordenadas not in repetidos:
        repetidos[coordenadas] = []
    #Guardar el índice del pez
    repetidos[coordenadas].append(int(idx))
#print(repetidos)

#Seleccionar el pez con mayor peso en repetidos
sobrevivientes = []
for peces in repetidos.values():
    #Buscamos el indice del mas pesado
    peso_max_idx = int(peces[np.argmax(weights[peces])])
    #Lo agregamos a la lista de salida
    sobrevivientes.append(peso_max_idx)

print("Los indices de los peces sobrevivientes fueron:", sobrevivientes)