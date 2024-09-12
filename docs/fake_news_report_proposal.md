
## 1.Title and Author

**Project Title:** Identifying and Classifying Fake News with Machine Learning

**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang

**Author Name:** Saivarun Kotha

**GitHub Repo:** [(https://github.com/saivarunkotha/UMBC-DATA606-Capstone/tree/main)]

**LinkedIn Profile:** [(https://www.linkedin.com/in/kothasaivarun/)]


---

## 2.Background

### What is it about?

This project focuses on detecting and classifying fake news using machine learning techniques(mainly SVM)and MLP techniques. The increase in the amount of misleading and fabricated news on the internet has raised many concerns about its societal and political implications, and ability to identify fake news. The goal is to create an accurate model for distinguishing real/fake news. 

### Why does it matter?

Fake news can influence public opinion, change facts, and lead to significant consequences in areas such as politics, health. The spread of misinformation is increased greatly by the social media. It is essential to develop efficient and reliable models to identify and classify false information to maintain the integrity of information consumed by the public.

### Research Questions:

1. Can we accurately classify news articles as real/fake using SVM model?
2. Which machine learning models perform best in classifying news articles as fake or real(using metrics such as accuracy, precision, recall)?
3. Can we use any NLP techniques such as TF-IDF and sentiment analysis to enhance the model's performance?
4. How can we improve the accuracy of fake news detection?

---

## 3.Data

### Data sources:

The dataset used for this project was obtained from an kaggle repository consisting of fake and real news articles. The dataset is pre-labeled for binary classification, where the target variable represents whether a news article is fake or real.

### Data size:

- The dataset is approximately 25MB in size.

### Data shape:

- The dataset has **9,900 rows** and **2 columns**.


### What does each row represent?

- Each row represents a news article, with the article's content and a corresponding label indicating whether the news is classified as "Fake" or "Real."

### Data dictionary:

| **Column Name** | **Data Type** | **Definition**                                  | **Potential Values**          |
|-----------------|---------------|------------------------------------------------|-------------------------------|
| Text            | Object        | The full text of the news article              | Text data                     |
| Label           | Object        | The classification of the news as real or fake | Categorical ("Fake", "Real")  |

### Target variable:

- The target/label in the machine learning model will be the **"Label"** column, which indicates whether the news is fake or real.

### Features/Predictors:

- The primary predictor will be the **"Text"** column, from which features such as word frequency, sentiment, and various NLP-derived statistics can be extracted for the model.
