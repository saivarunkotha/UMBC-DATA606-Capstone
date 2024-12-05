import streamlit as st
import pandas as pd
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load the dataset
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Preprocessing function
def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)  # Remove all non-word characters
    text = text.lower()  # Lowercase the text
    return text

# Load model and vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    with open('tfidf_vectorizer.pkl', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)
    with open('logistic_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return vectorizer, model

# Streamlit App Structure
st.title("Fake News Detection App")
st.write("Upload a CSV file with news articles or input custom text to check if it's real or fake.")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    data = load_data(uploaded_file)
    st.write("Preview of the uploaded data:")
    st.dataframe(data.head())
    st.write("Applying the model on the dataset...")

    vectorizer, model = load_model_and_vectorizer()
    data['text_processed'] = data['text'].apply(preprocess_text)
    X = vectorizer.transform(data['text_processed'])
    predictions = model.predict(X)

    data['Prediction'] = predictions
    st.write("Prediction results:")
    st.dataframe(data[['title', 'Prediction']])

# Custom Text Input
st.write("Or, input custom text below:")
custom_text = st.text_area("Enter the news article text here...")

if st.button("Check"):
    if custom_text:
        vectorizer, model = load_model_and_vectorizer()
        processed_text = preprocess_text(custom_text)
        input_vector = vectorizer.transform([processed_text])
        prediction = model.predict(input_vector)[0]
        result = "Fake" if prediction == 0 else "Real"
        st.write(f"The given text is classified as: **{result}**")
    else:
        st.write("Please enter some text to check.")
