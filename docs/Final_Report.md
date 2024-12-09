# Fake News Detection Using SVM

## 1. Title and Author

- Project Title: Fake News Detection Using SVM
- Prepared for: UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- Author Name: Saivarun Kotha
-  [GitHub Repository Link](https://github.com/saivarunkotha/UMBC-DATA606-Capstone/tree/main)
- [LinkedIn Profile](https://www.linkedin.com/in/kothasaivarun/)
- [PowerPoint Presentation Link](https://docs.google.com/presentation/d/1p_5e1AZjwhkqdMMwesVnIEe9rtcWYqdricBpvcqyx50/edit?usp=sharing)
- [YouTube Video Link](https://youtu.be/7xtKX4Ix9AQ)

## 2. Background
### What is it about?
This project focuses on detecting and classifying fake news using machine learning techniques(mainly SVM)and MLP techniques. The increase in the amount of misleading and fabricated news on the internet has raised many concerns about its societal and political implications, and ability to identify fake news. The goal is to create an accurate model for distinguishing real/fake news.

### Why does it matter?
Fake news can influence public opinion, change facts, and lead to significant consequences in areas such as politics, health. The spread of misinformation is increased greatly by the social media. It is essential to develop efficient and reliable models to identify and classify false information to maintain the integrity of information consumed by the public.

### Research Questions:
Can we accurately classify news articles as real/fake using SVM model?
- Which machine learning models perform best in classifying news articles as fake or real(using metrics such as accuracy, precision, recall)?
- Can we use any NLP techniques such as TF-IDF and sentiment analysis to enhance the model's performance?
- How can we improve the accuracy of fake news detection?

## 3. Data

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

## 4. Exploratory Data Analysis (EDA)

- Summary statistics were generated for article lengths, showing significant variance between real and fake articles..
- Visualizations, including histograms and bar plots, were created using Plotly Express to illustrate distributions, such as article length and the frequency of common words.
- Investigated missing values and duplicate rows.
    - Summary statistics revealed insights into numerical variable distributions.
    - Visualizations provided a graphical representation of variable distributions and potential relationships.
    - Text preprocessing included normalization, stopword removal, and tokenization, ensuring the data was ready for machine learning.
Checked for missing values and duplicates. No significant issues were found
    - The resulting dataset was structured such that each row represented a unique news article, and each column represented a distinct property of that article.

## 5. Model Training

Two machine learning models were used for predictive analysis:
- **Support Vector Machine (SVM)**
- **Logistic Regression**

The dataset was split into **80% training** and **20% testing**. 

- **Python packages used**: Scikit-learn, Pandas, and NLTK.
- **Development environment**: Jupyter Notebook and Streamlit for deployment.
- **Model Performance Evaluation**: Accuracy, Precision, Recall, and F1 Score were used to evaluate the models.

The dataset was split into **80% training** and **20% testing**. 

- **Python packages used**: Scikit-learn, Pandas, and NLTK.
- **Development environment**: Jupyter Notebook and Streamlit for deployment.
- **Model Performance Evaluation**: Accuracy, Precision, Recall, and F1 Score were used to evaluate the models.

## 6. Application of the Trained Models

A web application was developed using **Streamlit** to enable users to interact with the trained models.
- Users can input a news article, and the app will classify it as either "Real" or "Fake".
- The app provides a user-friendly interface, making the solution accessible to non-technical audiences.

## 7. Conclusion

This project successfully built a machine learning model to detect fake news, making it accessible through a web application. Despite promising results, the model could be improved by using larger datasets and more advanced models, such as neural networks. 

Key limitations include potential biases in the dataset and the limitation of using textual features only. Future research could explore incorporating metadata or using more sophisticated models like transformers.

## 8. References

- Pathak, R., & Patil, S. (2019). Fake News Detection Using Machine Learning. IEEE Xplore.
- Shu, K., et al. (2017). Fake News Detection on Social Media: A Data Mining Perspective. ACM Digital Library.
- Bird, S., et al. (2009). Natural Language Processing with Python. O'Reilly Media.
- Streamlit Documentation. (2023). Streamlit: Turn Data Scripts into Sharable Web Apps.
