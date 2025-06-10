import pandas as pd
import matplotlib.pyplot as plt
from langdetect import detect
from langdetect.lang_detect_exception import  LangDetectException


merged_df = pd.read_csv("/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/data/merged_df.csv")



def detect_lang(text) :
    try:
        return detect(str(text))
    except LangDetectException:
        return "unknown"

merged_df["detected_lang"] = merged_df["app_desc"].apply(detect_lang)


merged_df[["track_name_x", "detected_lang"]].head(10)

lang_counts = merged_df["detected_lang"].value_counts()

plt.figure(figsize=(12,6))
lang_counts.plot(kind = "bar",color = "skyblue")
plt.title("Açıklama Metinlerine göre tespit edilen diller")
plt.xlabel("Dil")
plt.ylabel("Uygulama Sayısı")
plt.savefig("/Users/muratsamanci/PycharmProjects/mobileappsanlaysis/visuals/dectected_languages_distribution.png")
plt.show()