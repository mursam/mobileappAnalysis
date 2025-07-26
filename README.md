# AI-Backed Mobile App Analysis  
Natural Language Processing, Exploratory Data Analysis and Visualization on Apple Store Dataset

## Project Description

This project focuses on exploring and analyzing mobile applications from the Apple Store dataset with the help of AI-powered tools and NLP techniques. It aims to uncover insights into user behavior, app categories, and app descriptions by combining data exploration, language detection, and natural language processing.

## Core Features

| Module | Description |
|--------|-------------|
| `01_data_exploration.py` | Loads and merges `AppleStore.csv` and `appleStore_description.csv`, performs basic structure exploration. |
| `02_category_analysis.py` | Visualizes category distribution, average user ratings, and download counts per genre. |
| `03_description_nlp.py` | Cleans app descriptions, removes stopwords, generates a WordCloud, and highlights most frequent keywords. |
| `lang_detection.py` | Detects the language of each app description using `langdetect` and visualizes the results. |

## Dataset Sources

- `AppleStore.csv` – Metadata of apps including name, rating, genre, downloads.
- `appleStore_description.csv` – App description texts matched by unique `id`.

These files are merged on the `id` field into a single dataset: `merged_df.csv`.

## Tech Stack and Libraries

- Python 3.x
- pandas, matplotlib, seaborn – Data processing and visualization
- nltk, wordcloud – NLP and text visualization
- langdetect – Language detection
- (Optional for future work: Hugging Face Transformers, BERTopic, Streamlit)

## Folder Structure

```
project-root/
│
├── data/                         # Raw and merged datasets
│   ├── AppleStore.csv
│   ├── appleStore_description.csv
│   └── merged_df.csv
│
├── visuals/                      # Saved plots and WordClouds
│   └── *.png
│
├── 01_data_exploration.py
├── 02_category_analysis.py
├── 03_description_nlp.py
├── lang_detection.py
└── README.md
```

## Example Visuals

- Top App Categories by Count
- Average User Ratings per Category
- WordCloud from App Descriptions
- Detected Language Distribution

All visuals are saved under the `visuals` folder.

## Potential Improvements

- Add sentiment analysis using pre-trained models
- Extract summaries or keywords from descriptions with LLMs
- Apply topic modeling (e.g. LDA or BERTopic)
- Build an interactive dashboard with Streamlit or Dash

## Use Cases

- Competitor analysis for mobile app companies such as AppNation or Codeway Studios
- User feedback mining for product teams
- App Store Optimization (ASO) using NLP insights

## Author

**Murat Samancı**  
Master’s Student in Artificial Intelligence  
Data Analyst | NLP and Growth Analytics Enthusiast  
LinkedIn: https://www.linkedin.com/in/muratsamanci/  
GitHub: https://github.com/muratsamanci  
Email: muratsamanci037@gmail.com
