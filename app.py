# app.py

import streamlit as st
import pandas as pd
import pickle

# Load the trained model and vectorizer
with open('recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load the dataset for resource details
df = pd.read_csv('legal_aid_resources_1000.csv')

# Function to get recommendations based on the case type and location
def get_recommendations(case):
    # Vectorize the case description
    case_vectorized = vectorizer.transform([case])
    
    # Get the nearest neighbors using the model's kneighbors method
    distances, indices = model.kneighbors(case_vectorized, n_neighbors=5)  # Get top 5 neighbors
    
    # Retrieve the corresponding resources for the nearest neighbors
    recommended_resources = df.iloc[indices[0]]  # Retrieve the full row for the top neighbors
    
    return recommended_resources

# Streamlit app UI
st.set_page_config(page_title="Legal Aid Resource Recommender", page_icon="⚖️", layout="centered")

# Title and description
st.title("Legal Aid Resource Recommender")
st.markdown("""
Welcome to the **Legal Aid Resource Recommender** app!  
Simply input your **Case Type**, **City**, and **State**, and we will recommend helpful legal resources such as NGOs, helplines, and legal clinics in your area.
""")

# Sidebar for user input
st.sidebar.header("Input Case Details")
case_type = st.sidebar.text_input("Enter Case Type (e.g., Family Dispute, Civil Case, etc.)")
city = st.sidebar.text_input("Enter City")
state = st.sidebar.text_input("Enter State")

# Button to trigger recommendation
if st.sidebar.button("Get Recommendations"):

    if case_type and city and state:
        # Combine inputs to create a recommendation query
        case_query = f"{case_type} {city} {state}"

        # Display a loading spinner while getting recommendations
        with st.spinner("Fetching recommendations..."):
            recommendations = get_recommendations(case_query)
        
        # Display the results
        st.subheader("Recommended Resources:")
        
        if len(recommendations) > 0:
            for idx, resource in recommendations.iterrows():
                st.markdown(f"### {resource['Resource_Name']}")
                st.write(f"**Case Type**: {resource['Case_Type']}")
                st.write(f"**Resource Type**: {resource['Resource_Type']}")
                st.write(f"**Contact**: {resource['Contact']}")
                st.markdown("---")
        else:
            st.write("Sorry, no recommendations found for your query.")
    else:
        st.warning("Please fill in all the fields to get recommendations.")

# Footer
st.markdown("---")
st.markdown("""
    Made with ❤️ by Legal Aid Team | [GitHub Repository](https://github.com/your-repo-link)
""")
