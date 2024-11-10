import json
import joblib

# Load compliance rules from JSON
def load_compliance_rules(file_path="compliance_rules.json"):
    with open(file_path, "r") as f:
        return json.load(f)

# Load the trained ML model for confidentiality detection
def load_confidential_model(model_path="confidential_model.pkl"):
    return joblib.load(model_path)

# Initialize the model
confidential_model = load_confidential_model()

# Function to predict if text is confidential using the ML model
def check_confidentiality(text, model):
    prediction = model.predict([text])[0]
    return "confidential" if prediction == 1 else "not confidential"

def check_compliance_rules(text, rules=None):
    """Check text for compliance issues based on rules and ML model."""
    if rules is None:
        rules = load_compliance_rules()

    compliance_issues = []

    # Rule-based compliance term detection
    for term, message in rules.items():
        if term in text.lower():
            compliance_issues.append(message)

    # Model-based confidentiality check
    confidentiality = check_confidentiality(text, confidential_model)
    if confidentiality == "confidential" and "confidential" not in compliance_issues:
        compliance_issues.append("Confidentiality issue flagged by ML model")

    return compliance_issues
