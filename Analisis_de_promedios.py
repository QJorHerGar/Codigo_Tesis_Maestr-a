#import numpy as np
import pandas as pd

def sort_data(df):    #Ordena tod y deja el gen hosekeeping y el Vh al principio, Despues quedan los demas genes
    df1 = df.replace({'GAPDH':'AAAA','cAMP':'CAMP'})
    df2 = df1.sort_values(by=['Target'],ascending=False).replace({'AAAA':'GAPDH'})
    df3 = pd.DataFrame()
    for i in range(0,25,6): 
        df3 = pd.concat([df2[i:i+6].sort_values(by='Sample',ascending=False),df3],ignore_index=True)
    return df3.reset_index()[['Target','Sample','Cq Mean']].replace({'CAMP':'cAMP'}) #El cambio de cAMP es por que c va despues que V por ser minuscula
                                                            # y Necesito que aparezca primero Vh para hcacer la resta
def D_Ct(df):
    df_final = df[['Target','Sample','Cq Mean']]
    df_final = df.rename({'Target':'Gen','Sample':'Tratamiento'},axis=1)
    df_final['GAPDH'] = df_final['Cq Mean'][df.index%6].to_list()
    df_final['Δ Ct'] = df_final['Cq Mean'] - df_final['GAPDH']
    return df_final.drop(range(0,6))[['Gen','Tratamiento','Δ Ct']].reset_index().drop('index',axis=1)

data1_1 = pd.read_csv("<DIRECCION HASTA DONDE ESTEN LOS DATOS YA DEPURADOS DE LA PLACA>/Rep 1 placa 1.csv").drop('Unnamed: 0',axis=1)
data1_2 = pd.read_csv("<DIRECCION HASTA DONDE ESTEN LOS DATOS YA DEPURADOS DE LA PLACA>/Rep 1 placa 2.csv").drop('Unnamed: 0',axis=1)
data2_1 = pd.read_csv("<DIRECCION HASTA DONDE ESTEN LOS DATOS YA DEPURADOS DE LA PLACA>/Rep 2 placa 1.csv").drop('Unnamed: 0',axis=1)
data2_2 = pd.read_csv("<DIRECCION HASTA DONDE ESTEN LOS DATOS YA DEPURADOS DE LA PLACA>/Rep 2 placa 2.csv").drop('Unnamed: 0',axis=1)
data3_1 = pd.read_csv("<DIRECCION HASTA DONDE ESTEN LOS DATOS YA DEPURADOS DE LA PLACA>/Rep 3 placa 1.csv").drop('Unnamed: 0',axis=1)
data3_2 = pd.read_csv("<DIRECCION HASTA DONDE ESTEN LOS DATOS YA DEPURADOS DE LA PLACA>/Rep 3 placa 2.csv").drop('Unnamed: 0',axis=1)
data4_1 = pd.read_csv("<DIRECCION HASTA DONDE ESTEN LOS DATOS YA DEPURADOS DE LA PLACA>/Rep 4 placa 1.csv").drop('Unnamed: 0',axis=1)
data4_2 = pd.read_csv("<DIRECCION HASTA DONDE ESTEN LOS DATOS YA DEPURADOS DE LA PLACA>/Rep 4 placa 2.csv").drop('Unnamed: 0',axis=1)
data5_1 = pd.read_csv("<DIRECCION HASTA DONDE ESTEN LOS DATOS YA DEPURADOS DE LA PLACA>/Rep 5 placa 1.csv").drop('Unnamed: 0',axis=1)
data5_2 = pd.read_csv("<DIRECCION HASTA DONDE ESTEN LOS DATOS YA DEPURADOS DE LA PLACA>/Rep 5 placa 2.csv").drop('Unnamed: 0',axis=1)

#### HAY QUE DIFERENCIAR ENTRE LA MEDICION DEL GEN HOSEKEEPER PLACA 1 Y EL GEN HOSEKEEPER PLACA 2 

data1_1 = data1_1.drop('Cq Std. Dev',axis = 1).dropna()
data1_2 = data1_2.drop('Cq Std. Dev',axis = 1).dropna()
data2_1 = data2_1.drop('Cq Std. Dev',axis = 1).dropna()
data2_2 = data2_2.drop('Cq Std. Dev',axis = 1).dropna()
data3_1 = data3_1.drop('Cq Std. Dev',axis = 1).dropna()
data3_2 = data3_2.drop('Cq Std. Dev',axis = 1).dropna()
data4_1 = data4_1.drop('Cq Std. Dev',axis = 1).dropna()
data4_2 = data4_2.drop('Cq Std. Dev',axis = 1).dropna()
data5_1 = data5_1.drop('Cq Std. Dev',axis = 1).dropna()
data5_2 = data5_2.drop('Cq Std. Dev',axis = 1).dropna()

#Union de los datos de todas las repeticiones y de paso quitamos la desv est
#data1 = data1_1.merge(data1_2,how='outer').drop('Cq Std. Dev',axis=1)
#data2 = data2_1.merge(data2_2,how='outer').drop('Cq Std. Dev',axis=1)
#data3 = data3_1.merge(data3_2,how='outer').drop('Cq Std. Dev',axis=1)
#data4 = data4_1.merge(data4_2,how='outer').drop('Cq Std. Dev',axis=1)
#data5 = data5_1.merge(data5_2,how='outer').drop('Cq Std. Dev',axis=1)

#Hay que homogenizar los nombres

data1_1 = data1_1.replace({'AMPc':'cAMP','Vehiculo':'Vh','Actina':'GAPDH','DC1':'YTHDC1'})  # Aqui use Actina en lugar de GAPDH
data1_2 = data1_2.replace({'AMPc':'cAMP','Vehiculo':'Vh'})
data2_1 = data2_1.replace({'E+M':'E2 + MPA'})
data2_2 = data2_2.replace({'E+M':'E2 + MPA'})
data3_1 = data3_1.replace({'E+M':'E2 + MPA'})
data3_2 = data3_2.replace({'E+M':'E2 + MPA'})
data4_1 = data4_1.replace({'E2+MPA':'E2 + MPA'})
data4_2 = data4_2.replace({'E2+MPA':'E2 + MPA'})
data5_1 = data5_1.replace({'E2+MPA':'E2 + MPA'})
data5_1 = data5_1.replace({'Duda 1':'E2','Duda 2':'E2 + MPA','Duda 3':'MPA'})
data5_2 = data5_2.replace({'E2+MPA':'E2 + MPA'})

data1_1 = D_Ct(sort_data(data1_1))
data1_2 = D_Ct(sort_data(data1_2))
data2_1 = D_Ct(sort_data(data2_1))
data2_2 = D_Ct(sort_data(data2_2))
data3_1 = D_Ct(sort_data(data3_1))
data3_2 = D_Ct(sort_data(data3_2))
data4_1 = D_Ct(sort_data(data4_1))
data4_2 = D_Ct(sort_data(data4_2))
data5_1 = D_Ct(sort_data(data5_1))
data5_2 = D_Ct(sort_data(data5_2))



# Haremos un experimento a partir de aqui, tratando de unir todos los datos
data1 = data1_1.merge(data1_2,how='outer')
data2 = data2_1.merge(data2_2,how='outer')
data3 = data3_1.merge(data3_2,how='outer')
data4 = data4_1.merge(data4_2,how='outer')
data5 = data5_1.merge(data5_2,how='outer')

#print(data1)
#print('--------------------------------------------------')
#print(data2)
#print('--------------------------------------------------')
#print(data3)
#print('--------------------------------------------------')
#print(data4)
#print('--------------------------------------------------')
#print(data5)
#print('--------------------------------------------------')

data1a2 = pd.concat([data1,data2],ignore_index=True)
data1a3 = pd.concat([data1a2,data3],ignore_index=True)
data1a4 = pd.concat([data1a3,data4],ignore_index=True)
data1a5 = pd.concat([data1a4,data5],ignore_index=True).dropna()


#data1a5 = data1a5.sort_values(by='Sample',ascending=False)
#data1a5 = data1a5.sort_values(by='Target',ascending=False)

data1a5.to_csv('Todas las PCR.csv')

genes_mean = data1a5.groupby(['Gen','Tratamiento'])['Δ Ct'].mean().rename('Full Mean') #Se obtiene el promedio 
genes_std = data1a5.groupby(['Gen','Tratamiento'])['Δ Ct'].std().rename('Full Std. Dev')   #SE obtiene la desv est

Ct_final = genes_mean.unstack().drop('ALKBH5') #Divide el indice multiple en una tabla
Ct_std = genes_std.unstack()


#Analisis por gen individual

YTHDF3 = data1a5.query("Gen == 'YTHDF3'")[['Gen','Tratamiento','Δ Ct']].sort_values(by=['Tratamiento'])
YTHDF3 = YTHDF3.drop([66,70])
YTHDF3_mean = YTHDF3.groupby('Tratamiento')['Δ Ct'].mean() 
YTHDF3_std = YTHDF3.groupby('Tratamiento')['Δ Ct'].std()


YTHDC1 = data1a5.query("Gen == 'YTHDC1'")[['Gen','Tratamiento','Δ Ct']].sort_values(by=['Tratamiento'])
YTHDC1 = YTHDC1.drop([40,39,38,37,36,41,22,231,86,229,18,233,230,136])
YTHDC1_mean = YTHDC1.groupby('Tratamiento')['Δ Ct'].mean() 
YTHDC1_std = YTHDC1.groupby('Tratamiento')['Δ Ct'].std()

YTHDF1 = data1a5.query("Gen == 'YTHDF1'")[['Gen','Tratamiento','Δ Ct']].sort_values(by=['Tratamiento'])
YTHDF1 = YTHDF1.drop([142,141,140,139,138,143])
YTHDF1_mean = YTHDF1.groupby('Tratamiento')['Δ Ct'].mean() 
YTHDF1_std = YTHDF1.groupby('Tratamiento')['Δ Ct'].std()

METTL3 = data1a5.query("Gen == 'METTL3'")[['Gen','Tratamiento','Δ Ct']].sort_values(by=['Tratamiento'])
METTL3 = METTL3.drop([208,207,63,14,205,204,206])
METTL3_mean = METTL3.groupby('Tratamiento')['Δ Ct'].mean() 
METTL3_std = METTL3.groupby('Tratamiento')['Δ Ct'].std()

FTO = data1a5.query("Gen == 'FTO'")[['Gen','Tratamiento','Δ Ct']].sort_values(by=['Tratamiento'])
FTO = FTO.drop([24,25,26,27,28,29,76,123,121,197])
FTO_mean = FTO.groupby('Tratamiento')['Δ Ct'].mean() 
FTO_std = FTO.groupby('Tratamiento')['Δ Ct'].std()

IGF2BP2 = data1a5.query("Gen == 'IGF2BP2'")[['Gen','Tratamiento','Δ Ct']].sort_values(by=['Tratamiento'])
IGF2BP2 = IGF2BP2.drop([220,219,218,217,221])
IGF2BP2_mean = IGF2BP2.groupby('Tratamiento')['Δ Ct'].mean() 
IGF2BP2_std = IGF2BP2.groupby('Tratamiento')['Δ Ct'].std()

IGFBP1 = data1a5.query("Gen == 'IGFBP1'")[['Gen','Tratamiento','Δ Ct']].sort_values(by=['Tratamiento'])
IGFBP1 = IGFBP1.drop([10,57,8,6,59,201,200,55,179])
IGFBP1_mean = IGFBP1.groupby('Tratamiento')['Δ Ct'].mean() 
IGFBP1_std = IGFBP1.groupby('Tratamiento')['Δ Ct'].std()

PRL = data1a5.query("Gen == 'PRL'")[['Gen','Tratamiento','Δ Ct']].sort_values(by=['Tratamiento'])
PRL = PRL.drop([130,226,225,80,127,161,159,131,79,31])
PRL_mean = PRL.groupby('Tratamiento')['Δ Ct'].mean() 
PRL_std = PRL.groupby('Tratamiento')['Δ Ct'].std()


#print(PRL)
#print('_________________')
#print(PRL_mean)
#print('_________________')
#print(PRL_std)

lista_anormales = [66,70,40,39,38,37,36,41,22,231,86,229,18,233,230,136,142,141,140,139,138,143,208,207,63,14,205,204,206,24,25,26,27,28,29,76,123,121,197,220,219,218,217,221,10,57,8,6,59,201,200,55,179,130,226,225,80,127,161,159,131,79,31]
#Genes discriminados por su alta dispersion.



#print(Ct_final)
#print('-----------------------------------------------------')
#print(Ct_std)
#print('-----------------------------------------------------')
#print(data1a5.head())
genes_mean = data1a5.groupby(['Gen','Tratamiento'])['Δ Ct'].mean().rename('Full Mean') #Se obtiene el promedio 
genes_std = data1a5.groupby(['Gen','Tratamiento'])['Δ Ct'].std().rename('Full Std. Dev')   #SE obtiene la desv est

Ct_final = genes_mean.unstack().drop('ALKBH5') #Divide el indice multiple en una tabla
Ct_std = genes_std.unstack()

print(Ct_final)
print(Ct_std)


Ct_final.to_csv('D_Ct Mean.csv')
Ct_std.to_csv('D_Ct Std.csv')



Dct = data1a5.drop(lista_anormales)
Dct.to_csv('DCt sin tratar.csv')
data1a5.to_csv('Dct sin filtrar.csv')

print(Dct)


