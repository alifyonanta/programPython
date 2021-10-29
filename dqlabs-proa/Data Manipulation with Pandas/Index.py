import pandas as pd
# Baca file sample_tsv.tsv untuk 10 baris pertama saja
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="/t", nrows=10)
# Index dari df
print("Index:", df.index)
# Column dari df
print("Columns:", df.columns)
# Set multi index df
df_x = df.set_index(['order_date','city','customer_id'])
# Print nama dan level dari multi index
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name,':',level)
# Cetak data frame awal
print("Dataframe awal:\n", df)
# Set index baru
df.index = ["Pesanan ke-" + str(i) for i in range(1, 11)]
# Cetak data frame dengan index baru
print("Dataframe dengan index baru:\n", df)

df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t", index_col=["order_date","order_id"])
# Cetak data frame untuk 8 data teratas
print("Dataframe:\n", df.head(8))
