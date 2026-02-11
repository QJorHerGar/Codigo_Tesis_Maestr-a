import pandas as pd

data = pd.read_csv("<Direcci[on hasta el recopilado de todas las PCR>/Todas las PCR.csv")

#Hay que hacer un indice primero para genes y despues para tratamientos

dudas = {'Duda 1':'E2',
         'Duda 2':'E2 + MPA',
         'Duda 3':'MPA'}

genes = data[['Target','Sample','Cq Mean']].replace({'DC1':'YTHDC1'})     #Se remplaza DC1 por el nombre completo, debido a un error
genes = genes.replace(dudas)

genes_mean = genes.groupby(['Target','Sample'])['Cq Mean'].mean().rename('Full Mean') #Se obtiene el promedio 
genes_std = genes.groupby(['Target','Sample'])['Cq Mean'].std().rename('Full Std. Dev')   #SE obtiene la desv est

###### Curado genes tratamiento E2

Ct_final = genes_mean.unstack() #Divide el indice multiple en una tabla

#genes_std1 = genes_std.unstack().drop(['Duda 1','Duda 2','Duda 3'],axis=1).dropna(axis=0) #Quita de la tabla las observaciones con una sola repeticion

#print(genes_std1.sort_values(by=['E2'],ascending=False)['E2'])
#print('-------------------------------------------------------')
#print(genes_std1.sort_values(by=['E2 + MPA'],ascending=False)['E2 + MPA'])
#print('-------------------------------------------------------')
#print(genes_std1.sort_values(by=['MPA'],ascending=False)['MPA'])
#print('-------------------------------------------------------')
#print(genes_std1.sort_values(by=['Mix'],ascending=False)['Mix'])
#print('-------------------------------------------------------')
#print(genes_std1.sort_values(by=['Vh'],ascending=False)['Vh'])
#print('-------------------------------------------------------')
#print(genes_std1.sort_values(by=['cAMP'],ascending=False)['cAMP'])
#print('-------------------------------------------------------')

#Aqui estan los sub Data Frames de cada gen por separado
YTHDF3 = genes.query("Target == 'YTHDF3'")[['Sample','Cq Mean']].sort_values(by=['Sample'])
YTHDC1 = genes.query("Target == 'YTHDC1'")[['Sample','Cq Mean']].sort_values(by=['Sample'])
FTO = genes.query("Target == 'FTO'")[['Sample','Cq Mean']].sort_values(by=['Sample'])
PRL = genes.query("Target == 'PRL'")[['Sample','Cq Mean']].sort_values(by=['Sample'])
IGFBP1 = genes.query("Target == 'IGFBP1'")[['Sample','Cq Mean']].sort_values(by=['Sample'])
IGF2BP2 = genes.query("Target == 'IGF2BP2'")[['Sample','Cq Mean']].sort_values(by=['Sample'])
YTHDF1 = genes.query("Target == 'YTHDF1'")[['Sample','Cq Mean']].sort_values(by=['Sample'])
METTL3 = genes.query("Target == 'METTL3'")[['Sample','Cq Mean']].sort_values(by=['Sample'])
GAPDH = genes.query("Target == 'GAPDH'")[['Sample','Cq Mean']].sort_values(by=['Sample'])


#Analisis YTHDF3
#YTHDF3 = YTHDF3.drop([4,13,15,21,12,5,8])
#YTHDF3_mean = YTHDF3.groupby('Sample')['Cq Mean'].mean() 
#YTHDF3_std = YTHDF3.groupby('Sample')['Cq Mean'].std()

#print('-------------------------------------------------------')
#print(YTHDF3)
#print('-------------------------------------------------------')
#print(YTHDF3_mean)
#print(YTHDF3_std)


YTHDC1 = YTHDC1.drop([67,83,285])
YTHDC1_mean = YTHDC1.groupby('Sample')['Cq Mean'].mean() 
YTHDC1_std = YTHDC1.groupby('Sample')['Cq Mean'].std()

print('-------------------------------------------------------')
print(YTHDC1)
print('-------------------------------------------------------')
print(YTHDC1_mean)
print(YTHDC1_std)
