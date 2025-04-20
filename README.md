
## ⚖️ Legal Aid Resource Recommender

A smart legal aid tool that recommends legal resources (NGOs, helplines, legal clinics, etc.) based on the **case type** and **location** provided by the user. This project helps individuals easily access relevant legal support without manual searching.

---

### 📌 Features

- 🔍 Recommends resources based on **Case Type**, **City**, and **State**
- 🧠 Uses **K-Nearest Neighbors (KNN)** for similarity-based recommendations
- 🎯 User-friendly **Streamlit web interface**
- 📋 Displays **Resource Name**, **Case Type**, **Resource Type**, and **Contact Info**
- ✅ Lightweight, fast, and easy to use

---

### 📂 Dataset

The recommender is trained on a custom dataset with the following columns:

```csv
State,City,Case_Type,Resource_Name,Resource_Type,Contact,search_key
```

Example rows:
```
Delhi,New Delhi,Family Dispute,Women Rights NGO,NGO,+91-1234567890,Family Dispute New Delhi Delhi
Maharashtra,Mumbai,Civil Case,Legal Aid Mumbai,Legal Clinic,+91-9876543210,Civil Case Mumbai Maharashtra
```

---

### 🧠 Machine Learning Approach

- **Model:** `KNeighborsClassifier` (from `sklearn`)
- **Vectorization:** TF-IDF on a `search_key` column (a combination of case type and location)
- **Similarity-based recommendation:** The model finds the top similar entries from the dataset

---

### 🚀 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/legal-aid-recommender.git
cd legal-aid-recommender
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

Dependencies include:
- `pandas`
- `scikit-learn`
- `streamlit`

3. **Train the Model**

Make sure your dataset is named `legal_aid_resources_1000.csv` and run:

```bash
python train.py
```

This will generate:
- `recommendation_model.pkl`
- `vectorizer.pkl`

4. **Run the App**

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser to use the app.

---

### 💻 File Structure

```
📁 legal-aid-recommender/
│
├── app.py                   # Streamlit web app
├── train.py                 # Script to train the recommender model
├── check.py                 # Accuracy check script
├── legal_aid_resources_1000.csv   # Dataset
├── vectorizer.pkl           # Saved TF-IDF vectorizer
├── recommendation_model.pkl # Saved recommendation model
└── README.md                # You're here!
```

---


