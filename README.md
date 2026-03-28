# UMBC-DATA606-Capstone
# Fake News Detection Using Machine Learning

> A natural language processing pipeline that classifies news articles as **Real** or **Fake** using SVM and Logistic Regression — deployed as an interactive Streamlit web app.

**Author:** Saivarun Kotha  
**Program:** MS Data Science, UMBC — Capstone Project  
**Advisor:** Dr. Chaojie (Jay) Wang

[![LinkedIn](https://img.shields.io/badge/LinkedIn-kothasaivarun-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/kothasaivarun/)
[![GitHub](https://img.shields.io/badge/GitHub-saivarunkotha-black?style=flat&logo=github)](https://github.com/saivarunkotha/UMBC-DATA606-Capstone)
[![Presentation](https://img.shields.io/badge/Slides-Google%20Slides-orange?style=flat&logo=google)](https://docs.google.com/presentation/d/1p_5e1AZjwhkqdMMwesVnIEe9rtcWYqdricBpvcqyx50/edit?usp=sharing)
[![Demo](https://img.shields.io/badge/Demo-YouTube-red?style=flat&logo=youtube)](https://youtu.be/7xtKX4Ix9AQ)

---

## Problem statement

The rapid spread of misinformation on social media and online news platforms has become a serious societal challenge — influencing elections, public health decisions, and shaping public opinion. This project builds an automated fake news detection system that can classify a news article as **Real** or **Fake** with high accuracy, using only its text content.

---

## Dataset

| Property | Detail |
|---|---|
| Source | Kaggle — Fake and Real News Dataset |
| Size | ~25 MB |
| Rows | 9,900 articles |
| Columns | 2 (`text`, `label`) |
| Target | `label` — Binary: `"Fake"` or `"Real"` |
| Split | 80% training / 20% testing |

Each row represents a single news article. The `text` column contains the full article body; the `label` column is the ground-truth classification.

---

## Approach & methodology

### 1. Exploratory Data Analysis
- Analyzed article length distributions across fake vs. real news — significant variance found
- Visualized word frequency distributions and class balance using Plotly Express
- Checked for missing values and duplicates — dataset was clean

### 2. Text preprocessing (NLP pipeline)
- Lowercasing, punctuation removal, stopword removal
- Tokenization using NLTK
- TF-IDF vectorization to convert text into numerical features
- Sentiment analysis as an additional feature signal

### 3. Model training & comparison

Two models were trained and compared:

| Model | Accuracy 
|---|---|---|---|---|
| Support Vector Machine (SVM) | 94%
| Logistic Regression | 89%


- **Best model:** Support Vector Machine (SVM)
- **Evaluation metrics:** Accuracy, Precision, Recall, F1 Score

---

## Streamlit app

A web application was built with Streamlit that allows any user — technical or not — to test the model in real time.

**How it works:**
1. User pastes or types a news article into the input box
2. The app preprocesses the text through the same NLP pipeline used during training
3. The trained SVM model classifies the article as **Real** or **Fake**
4. Result is displayed instantly with a confidence indicator

**To run the app locally:**

```bash
# Clone the repo
git clone https://github.com/saivarunkotha/UMBC-DATA606-Capstone.git
cd UMBC-DATA606-Capstone

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app/app.py
```

---

## Repository structure

```
UMBC-DATA606-Capstone/
│
├── app/                  # Streamlit web application
├── data/                 # Dataset (or data loading scripts)
├── notebooks/            # EDA and model training notebooks
├── docs/                 # Project report and presentation assets
├── requirements.txt      # Python dependencies
└── README.md
```

---

## Key findings & conclusions

- SVM with TF-IDF features proved highly effective for binary text classification on this dataset
- Article length and word frequency distributions showed measurable differences between real and fake news
- TF-IDF outperformed raw word counts as a feature representation
- The Streamlit app makes the model accessible to non-technical users

**Limitations:**
- Model relies on text content only — metadata (author, source, publication date) could improve performance
- Dataset limited to ~9,900 articles; larger corpora may improve generalization
- Transformer-based models (BERT, RoBERTa) could significantly boost accuracy in future work

---

## Tech stack

`Python` &nbsp; `scikit-learn` &nbsp; `NLTK` &nbsp; `Pandas` &nbsp; `TF-IDF` &nbsp; `Streamlit` &nbsp; `Plotly` &nbsp; `Jupyter Notebook`

---

## References

- Pathak, R., & Patil, S. (2019). Fake News Detection Using Machine Learning. *IEEE Xplore.*
- Shu, K., et al. (2017). Fake News Detection on Social Media: A Data Mining Perspective. *ACM Digital Library.*
- Bird, S., et al. (2009). *Natural Language Processing with Python.* O'Reilly Media.
- Streamlit Documentation. (2023). Streamlit: Turn Data Scripts into Sharable Web Apps.
