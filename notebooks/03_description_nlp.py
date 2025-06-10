import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import re


nltk.download("stopwords")


merged_df = pd.read_csv("/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/data/merged_df.csv")
print(merged_df[["track_name_x","app_desc"]].head())

def clean_text(text) :
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.strip()
    return text


stop_words = set(stopwords.words("english"))

all_desc = " ".join(merged_df["app_desc"].dropna().apply(clean_text))

filtered_words = [word for word in all_desc.split() if word not in stop_words]




worldcloud_text = " ".join(filtered_words)

wordcloud = WordCloud(width=1200, height=600, background_color="white").generate(worldcloud_text)



plt.figure(figsize=(15,7))
plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
wordcloud.to_file("/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/visuals/app_desc_wordcloud.png")
plt.show()

from collections import Counter

word_counts = Counter(filtered_words)
print(word_counts.most_common(20))