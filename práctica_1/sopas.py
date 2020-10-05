# En este ejercicio deberá implementar la función `calcular` y verificar su correcto funcionamiento

import pandas as pd
import numpy as np

def verificar_resultado(expected, calculated, title):
    # Verifica si {expected} es igual a {calculated} con unna tolerancia de 1e-2 (dos decimales)
    tolerance = 1e-2
    title=title.ljust(35)
    if np.abs(expected-calculated)>tolerance:
        print(f"- {title}: error (esperaba {expected}, obtuve {calculated:.2f})")
    else:
        print(f"+ {title}: bien  (esperaba {expected}, obtuve {calculated:.2f}).")


# Retorna el indice de la lista en base a su key
def get_key(data, key):
    return list(data.keys()).index(key) 

def calcular(dataframe):
    # Arreglo en numpy
    sopas = np.array(dataframe)

    ###### 1) Calcular el valor promedio del atributo GRASA ######
    # Inicialización de datos
    promedio_grasa = 0
    # Obtengo la key de GRASA
    key_de_grasa = get_key(dataframe, 'GRASA')
    # Obtengo el promedio
    promedio_grasa = np.mean(sopas[:,key_de_grasa]) 
        # VERSION SIN NUMPY
        # cant_filas = len(dataframe)
        # for i in range(cant_filas):
        #     suma += sopas[i,key_de_grasa]
        # promedio_grasa = suma/cant_filas



    ######  2) Contar la cantidad sopas del tipo "CC" ######
    # Inicialización de datos
    cant_tipo_cc = 0
    # Obtengo la key de TIPO
    key_de_tipo = get_key(dataframe, 'TIPO')
    # Obtengo el promedio
    cant_tipo_cc = np.count_nonzero(sopas[:,key_de_tipo] == 'CC')



    ######  3) Encontrar la sopa con más sodio (y el valor) ######
    max_sodio = 0
    max_sodio_indice = 0

    key_de_sodio = get_key(dataframe, 'SODIO')
    max_sodio = np.amax(sopas[:,key_de_sodio])

    result = np.where(sopas == np.amax(sopas[:,key_de_sodio]))
    max_sodio_indice = int(result[0])

    ###### FIN COMPLETAR ######

    return promedio_grasa, cant_tipo_cc, max_sodio, max_sodio_indice


dataframe = pd.read_excel('Sopas.xls')

filas,columnas=dataframe.shape
print(f"El conjunto de datos tiene:\n\t {filas} filas o ejemplos\n\t {columnas} columnas o atributos")
print("Las columnas son: ", list(dataframe.columns))
print("\n")

# print)

promedio_grasa, cant_tipo_cc, max_sodio, max_sodio_indice = calcular(dataframe)
print("=== Resultado de los cálculos: ===")
verificar_resultado(2.4, promedio_grasa, "promedio_grasa")
verificar_resultado(15, cant_tipo_cc, "cant_tipo_cc")
verificar_resultado(970, max_sodio, "max_sodio")
verificar_resultado(6, max_sodio_indice, "max_sodio_indice")
