import pdfplumber
import spacy
import re

# Load the SpaCy model for NER
nlp = spacy.load("en_core_web_md")

def extract_stakeholder_info(pdf_path):
    # Step 1: Extract text from PDF
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

    # Step 2: Run SpaCy NER to find names
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

    # Step 3: Regex patterns for potential ID/passport numbers
    id_patterns = [
        r'\b[A-Z]{1,2}\d{6,8}\b',      # Alphanumeric passport-like IDs
        r'\b\d{8,10}\b'                # Numeric IDs with 8-10 digits
    ]
    ids = []
    for pattern in id_patterns:
        ids.extend(re.findall(pattern, text))

    # Deduplicate results to remove duplicates
    names = list(set(names))
    ids = list(set(ids))

    return {"names": names, "ids": ids}

# Example usage
# stakeholder_info = extract_stakeholder_info("path_to_pdf_file.pdf")
# print(stakeholder_info)
