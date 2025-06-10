import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os



pd.set_option('display.max_columns', None)

apple_store_path = '/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/data/AppleStore.csv'
description_path = 'data/appleStore_description.csv'

df_apps = pd.read_csv(apple_store_path)
df_desc = pd.read_csv(description_path)



print ("Applstore.csv veri seti boyutu:", df_apps.shape)
print ("Applestore_description  veri seti boyutu:", df_desc.shape)


print("\nApplstore.csv  kolonları : \n" , df_apps.columns)
print("\nApplestore_description  : \n" , df_apps.columns)

df_apps.head()
df_desc.head()


merged_df = pd.merge(df_apps,df_desc, on="id")
print("birleştirilmiş veri seti boyutu:", merged_df.shape)
merged_df.head()

# merged_df'i kaydet
os.makedirs("/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/data", exist_ok=True)
merged_df.to_csv("/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/data/merged_df.csv", index=False)

print("Birleştirilmiş veri başarıyla kaydedildi: data/merged_df.csv")
