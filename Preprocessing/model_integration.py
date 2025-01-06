import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Preprocessing Function
def preprocess_text(text):
    if not isinstance(text, str):
        return "no meaningful text"

    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    if len(tokens) > 5:
        tokens = [word for word in tokens if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    preprocessed_text = " ".join(tokens)

    return preprocessed_text if preprocessed_text.strip() else text

# Load Translated Dataset
def load_translated_dataset(path):
    dataset = pd.read_csv(path)
    dataset['Cleaned_Blurb'] = dataset['book_desc'].apply(preprocess_text)
    dataset['book_original_title'] = dataset['book_title']
    dataset['book_title'] = dataset['book_title'].apply(preprocess_text)
    return dataset

# TF-IDF Vectorizer
def create_tfidf_matrix(dataset):
    tfidf_vectorizer = TfidfVectorizer(
        max_features=10000,
        min_df=2,
        max_df=0.9,
        ngram_range=(1, 3),
        sublinear_tf=True
    )
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset['Cleaned_Blurb'])
    return tfidf_vectorizer, tfidf_matrix

# Recommend Function
def recommend_books_by_blurb(user_blurb, tfidf_vectorizer, tfidf_matrix, dataset, top_n=5):
    preprocessed_blurb = preprocess_text(user_blurb)
    if not preprocessed_blurb.strip():
        return "The input blurb is empty after preprocessing. Please provide a valid input."

    user_blurb_vector = tfidf_vectorizer.transform([preprocessed_blurb])
    similarity_scores = cosine_similarity(user_blurb_vector, tfidf_matrix).flatten()
    similar_indices = similarity_scores.argsort()[-top_n:][::-1]

    if similar_indices.size == 0:
        return "No similar books found."
    
    # print(dataset.iloc[similar_indices][['book_original_title', 'book_desc']].to_dict(orient='records'))

    return dataset.iloc[similar_indices][['book_original_title', 'book_desc']].to_dict(orient='records')
