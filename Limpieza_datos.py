import pandas as pd
#import numpy as np

data = pd.read_csv("<DIRECCION HASTA EL ARCHIVO CSV>/Rep 5 placa 2.csv")

new_index = ['Target','Content','Sample','Cq', 'Cq Mean','Cq Std. Dev']

data1 = data[new_index] #Deja el df con unicamente las columnas de interes

#promedios = data1.groupby('Content')['Cq'].mean()    #agrupa mediante hacer el promedio de la columna Cq de todo lo que 
                                                      #Sea igual en la columna Content

data2 = data1.sort_values(by=['Cq Std. Dev'],ascending = False)          #Agrupa por desviacion estandar

#print(data2[0:18])

##### A partir de aqui, se analiza cada caso para saber si hay que eliminar una replica. Se debe calcular nuevamente
# Desviacion estandar y promedio

data2_1 = data2.drop([73,80]) # Paraeliminar, es necesario a;adir una coma y el numero de cada renglon a eliminar.
       
data3 = data2_1[['Target','Content','Sample','Cq']].copy()       #Una copia, para no moverle al df inicial
data_mean = data3.groupby('Content')['Cq'].mean().rename('Cq Mean')   #Se aniaden columnas para promedio y desv est
data_std = data3.groupby('Content')['Cq'].std().rename('Cq Std. Dev')
## ahora con los nuevos promedios y desviacion estandar, se agrupan los datos para solo dejar Cq mean y Cq Std Dev

data4 = data3.merge(data_mean,how='left',on='Content')
data4 = data4.merge(data_std,how='left',on='Content').drop('Cq',axis=1)
data5 = data4.drop_duplicates().drop('Content',axis=1)


print(data5[0:15])
print(str('############################     ') + str(len(data5['Target'])) + str('      ###############') )
print(data2[0:21])

#data5.to_csv('Rep 5 Placa 2.csv')
