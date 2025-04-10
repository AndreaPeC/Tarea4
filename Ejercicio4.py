#Ejercicio 4

import numpy as np

#Generrar arrreglo de calificaciones de estudiantes
generator = np.random.default_rng(1010)
data = np.round (generator.uniform (low=0, high=101,size=10))
calificaciones = data
#calificaciones = np.random.randint(9, 101, size=10)
print("Las calificaciones fueron: ",calificaciones)

#Funcion para determinar valores menores a 60
def primeros3_menos_de60 (calificaciones):
    #Utilizando una mascara se buscaran cuales calificaciones son menores a 60
    bool_idx = (calificaciones < 60)
    #Seleccionamos los 3 primeros indices de calificaciones que cumplieron la condicion
    #print(np.where(bool_idx)[0])
    orden_entrega = np.where(bool_idx)[0][:3]
    #Reemplazamos la calificacion por 0
    calificaciones[orden_entrega] = 0
    return calificaciones

print(primeros3_menos_de60(calificaciones))