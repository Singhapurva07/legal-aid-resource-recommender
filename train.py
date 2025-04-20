# train.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle

# Load the dataset
df = pd.read_csv('legal_aid_resources_1000.csv')

# Combine 'Case_Type', 'City', and 'State' to create a feature for recommendation
df['case_location'] = df['Case_Type'] + ' ' + df['City'] + ' ' + df['State']

# Vectorize the combined feature using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['case_location'])

# Fit the Nearest Neighbors model to the vectorized data
model = NearestNeighbors(n_neighbors=5, metric='cosine')
model.fit(X)

# Save the model and vectorizer for future use
with open('recommendation_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved successfully.")
