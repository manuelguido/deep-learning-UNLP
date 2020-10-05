# En este ejercicio deberá implementar la función `calcular` y verificar su correcto funcionamiento
import numpy as np
import pandas as pd

dataframe = pd.read_csv('iris.csv')

df = pd.read_csv('iris.csv')

data = pd.plotting.scatter_matrix(df, alpha=0.2)

df.hist()
