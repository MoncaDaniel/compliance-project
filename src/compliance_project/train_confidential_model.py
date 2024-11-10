# In src/compliance_project/train_confidential_model.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib
from compliance_project.confidential_data import get_confidential_data


def train_confidential_model():
    data = get_confidential_data()
    texts = [item["text"] for item in data]
    labels = [1 if item["label"] == "confidential" else 0 for item in data]

    # Create a pipeline with a CountVectorizer and Logistic Regression
    model = make_pipeline(CountVectorizer(), LogisticRegression())
    model.fit(texts, labels)

    # Save the trained model to a file
    joblib.dump(model, "confidential_model.pkl")
    print("Confidential model trained and saved to confidential_model.pkl")

# Run this function if this script is run directly
if __name__ == "__main__":
    train_confidential_model()
