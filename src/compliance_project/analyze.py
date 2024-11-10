import spacy

# Load spaCy model for NLP analysis
nlp = spacy.load("en_core_web_md")

def extract_entities(text):
    """
    Extract relevant entities from the text, focusing on compliance-related entities.
    Filters out duplicates and unwanted entity types.
    """
    doc = nlp(text)
    relevant_entities = set()  # Use a set to avoid duplicate entries

    # Define entity labels relevant to compliance
    relevant_labels = {"ORG", "LAW", "PERSON"}

    # Extract entities and filter by type
    for ent in doc.ents:
        if ent.label_ in relevant_labels:
            relevant_entities.add((ent.text, ent.label_))

    # Convert set back to list for output
    return list(relevant_entities)
