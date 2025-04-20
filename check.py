# check.py

import pandas as pd
import pickle

# Load the trained model and vectorizer
with open('recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load the dataset again for comparison
df = pd.read_csv('legal_aid_resources_1000.csv')

# Function to get recommendations based on the case type and location
def get_recommendations(case):
    # Vectorize the case description
    case_vectorized = vectorizer.transform([case])
    
    # Get the nearest neighbors using the model's kneighbors method
    distances, indices = model.kneighbors(case_vectorized, n_neighbors=5)  # Get top 5 neighbors
    
    # Print distances and indices for debugging purposes
    print(f"Distances: {distances}")
    print(f"Indices: {indices}")
    
    # Retrieve the corresponding resources for the nearest neighbors
    recommended_resources = df.iloc[indices[0]]['Resource_Name'].values  # Retrieve Resource_Name for the top neighbors
    
    return recommended_resources

# Test case
test_case = 'Family Dispute Delhi Delhi'  # Change as needed
print(f"Test Case: {test_case}")
recommendations = get_recommendations(test_case)
print("Recommended Resources:")
print(recommendations)
