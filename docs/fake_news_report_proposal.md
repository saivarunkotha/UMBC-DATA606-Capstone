
## 1.Title and Author

**Project Title:** Identifying and Classifying Fake News with Machine Learning

**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang

**Author Name:** Saivarun Kotha

**GitHub Repo:** [(https://github.com/saivarunkotha/UMBC-DATA606-Capstone/tree/main)]

**LinkedIn Profile:** [(https://www.linkedin.com/in/kothasaivarun/)]


---

## 2.Background

### What is it about?

This project focuses on detecting and classifying fake news using machine learning techniques. The proliferation of misleading and fabricated news on the internet has raised concerns about its societal and political implications, making the ability to identify fake news crucial.

### Why does it matter?

Fake news can influence public opinion, distort facts, and lead to significant consequences in areas such as politics, health, and social behavior. It is essential to develop reliable methods to identify and classify false information to maintain the integrity of information consumed by the public.

### Research Questions:

1. Can we use NLP techniques to extract meaningful features from text to classify news articles as real or fake?
2. Which machine learning models perform best in classifying news articles as fake or real?
3. How can we improve the accuracy of fake news detection?

---

## 3.Data

### Data sources:

The dataset used for this project was obtained from an online source consisting of fake and real news articles. The dataset is pre-labeled for binary classification, where the target variable represents whether a news article is fake or real.

### Data size:

- The dataset is approximately 25MB in size.

### Data shape:

- The dataset has **9,865 rows** and **2 columns**.


### What does each row represent?

- Each row represents a single news article, with the article's content and a corresponding label indicating whether the news is classified as "Fake" or "Real."

### Data dictionary:

| **Column Name** | **Data Type** | **Definition**                                  | **Potential Values**          |
|-----------------|---------------|------------------------------------------------|-------------------------------|
| Text            | Object        | The full text of the news article              | Text data                     |
| Label           | Object        | The classification of the news as real or fake | Categorical ("Fake", "Real")  |

### Target variable:

- The target/label in the machine learning model will be the **"Label"** column, which indicates whether the news is fake or real.

### Features/Predictors:

- The primary predictor will be the **"Text"** column, from which features such as word frequency, sentiment, and various NLP-derived statistics can be extracted for the model.
