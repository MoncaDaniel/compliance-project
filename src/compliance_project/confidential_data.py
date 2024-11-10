# In src/compliance_project/confidential_data.py

def get_confidential_data():
    return [
        {"text": "This is a confidential report about the merger.", "label": "confidential"},
        {"text": "This information is strictly confidential and proprietary.", "label": "confidential"},
        {"text": "Unauthorized access to confidential documents is prohibited.", "label": "confidential"},
        {"text": "The quarterly sales report is for internal use only.", "label": "confidential"},
        {"text": "The company headquarters is located in New York.", "label": "not confidential"},
        {"text": "Our team will meet for lunch at 12 PM.", "label": "not confidential"},
        {"text": "The annual report will be available on the company website.", "label": "not confidential"},
        {"text": "Product specifications are publicly accessible.", "label": "not confidential"},
    ]
