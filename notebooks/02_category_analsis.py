import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

merged_df= pd.read_csv("/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/data/merged_df.csv")

merged_df.head(5)

category_counts = merged_df["prime_genre"].value_counts().sort_values(ascending=False)

print(category_counts)

# En çok uygulamaya sahip 10 kategori
plt.figure(figsize=(12,6))
sns.barplot(x=category_counts.head(10).values,y=category_counts.head(10).index,legend=True)
plt.title("En fazla Uygulamaya Sahip 10 kategori")
plt.xlabel("uygulama Sayısı")
plt.ylabel("kategori")
plt.savefig("/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/visuals/top_10_categories.png")

plt.show()


#Ortalama kullanıcı puanı en yüksek 10 kategori
category_ratings= merged_df.groupby("prime_genre")["user_rating"].mean().sort_values(ascending=False)
category_ratings.head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=category_ratings.head(10).values, y=category_ratings.head(10).index,color="red")
plt.title("Ortalama Kullanıcı puanı en yüksek 10 kategori")
plt.xlabel("ortalama Puan")
plt.ylabel("Kategori")
plt.show()
plt.savefig("/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/visuals/top_10_categories_user_rate.png")


## Ortalama indirme sayıları
category_downloads = merged_df.groupby("prime_genre")["rating_count_tot"].mean().sort_values(ascending=False)
print(category_downloads)

plt.figure(figsize=(12,6))
sns.barplot(x=category_downloads.head(10).values, y=category_downloads.head(10).index,color="green")
plt.title("Ortalama indirme sayısı en yüksek olan 10 kategori")
plt.xlabel("Ortalama İndirme Sayısı")
plt.ylabel("kategori")
plt.show()
plt.savefig("/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/visuals/top_10_categories_download.png")
