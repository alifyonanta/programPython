#import library
import pandas as pd
pd.options.display.max_columns = 50
#import dataset
df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')
#Tampilkan jumlah baris dan kolom
print(df_load.shape)
#Tampilkan 5 data teratas
print(df_load.head(5))
#Jumlah ID yang unik
print(df_load.customerID.nunique())

df_load['valid_id'] = df_load['customerID'].astype(str).str.match(r'(45\d{9,10})')
df_load = (df_load[df_load['valid_id']==True]).drop('valid_id',axis=1)
print('Hasil jumlah ID Customer yang terfilter adalah',df_load['customerID'].count())
