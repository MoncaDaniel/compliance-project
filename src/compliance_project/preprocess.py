import pdfplumber
import re
import spacy

# Load spaCy's default English stop words
nlp = spacy.blank("en")

def load_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text

def preprocess_text(text, remove_stopwords=True, lowercase=True):
    if lowercase:
        text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)  # Removes special characters
    if remove_stopwords:
        tokens = [word for word in text.split() if word not in nlp.Defaults.stop_words]
        text = ' '.join(tokens)
    return text

def get_pdf_metadata(file_path):
    """Extract metadata from a PDF file."""
    with pdfplumber.open(file_path) as pdf:
        metadata = pdf.metadata
    return metadata if metadata else {}
