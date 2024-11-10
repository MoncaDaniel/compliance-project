import json
from compliance_project.preprocess import load_pdf, preprocess_text, get_pdf_metadata
from compliance_project.analyze import extract_entities
from compliance_project.rules import check_compliance_rules
from compliance_project.stakeholders import extract_stakeholder_info  # Importing the new function

def main(file_path, output_path="output.json"):
    # Load and preprocess the document
    raw_text = load_pdf(file_path)
    cleaned_text = preprocess_text(raw_text)

    # Extract metadata, entities, and compliance issues
    metadata = get_pdf_metadata(file_path)
    entities = extract_entities(cleaned_text)
    compliance_issues = check_compliance_rules(cleaned_text)

    # Extract stakeholder information
    stakeholder_info = extract_stakeholder_info(file_path)

    # Prepare output in JSON format
    output_data = {
        "Metadata": metadata,
        "Entities": [{"text": ent[0], "label": ent[1]} for ent in entities],
        "Compliance Issues": compliance_issues,
        "Stakeholder Information": {
            "Names": stakeholder_info["Names"],
            "IDs": stakeholder_info["IDs"]
        }
    }

    # Save JSON output to a file
    with open(output_path, "w") as json_file:
        json.dump(output_data, json_file, indent=4)

    print(f"Output saved to {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path> [output_path]")
    else:
        file_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else "output.json"
        main(file_path, output_path)
