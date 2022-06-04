import matplotlib.pyplot as plt
import time as tm
import numpy as np
import datetime as dt
import pandas as pd
import csv
from mergesort import mergeSort

values = np.arange(10, 100000, 100)
tiempos = []
fechas = []
fecha_hora = dt.datetime.now()

for i in values:
    tiempo_inicio = tm.time()
    arreglo = list(np.random.randint(10000, size=(i)))
    mergeSort(arreglo)
    tiempo_final = tm.time()
    tiempos.append(tiempo_final-tiempo_inicio)
    fechas.append(fecha_hora)

minimo = min(tiempos)
maximo = max(tiempos)

df_tiempos = pd.DataFrame({
    'N':values,
    'Tiempos':tiempos,
    'Fecha':fechas
})

nombre_archivo = '{}_{}_{}-{}_{}_{}.csv'.format(fecha_hora.year, fecha_hora.month, fecha_hora.day,
                                            fecha_hora.hour, fecha_hora.minute, fecha_hora.second)

df_tiempos.to_csv(nombre_archivo)

plt.plot(values, tiempos, 'bo')
plt.show()