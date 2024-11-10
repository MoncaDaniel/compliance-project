# Compliance Analysis Project Documentation

## Introduction

The Compliance Analysis Project is designed to support compliance teams by analyzing PDF documents for sensitive information. This tool uses NLP techniques to extract named entities, check for compliance with predefined rules, and detect confidential information in text. It is aimed at organizations handling sensitive documents containing names, IDs, passport numbers, and other identifiable information.

Key objectives:
- Automatically detect sensitive information in PDF documents.
- Identify stakeholder information such as names and IDs.
- Provide rule-based compliance checks.

## Project Workflow

The project follows these main steps for each PDF document:

1. **PDF Loading and Preprocessing**: Load the PDF file and extract its text content.
2. **Metadata Extraction**: Extract metadata such as author and title (if available).
3. **Text Cleaning and Preprocessing**: Clean the extracted text for analysis.
4. **Named Entity Recognition**: Use NLP to identify named entities, including stakeholder names and ID numbers.
5. **Compliance Rule Checking**: Check the text against predefined compliance rules.
6. **Confidential Information Detection**: Use a trained machine learning model to detect confidential information.
7. **Output**: Generate a report with metadata, identified entities, and compliance issues.

### Preprocessing

The preprocessing pipeline is designed to handle PDF documents and ensure the text is suitable for analysis.

- **PDF Text Extraction**: Extracts text using PyPDF2.
- **Text Cleaning**: Removes non-alphabetic characters, converts text to lowercase, and normalizes whitespace.
- **Stop Words Removal** (if applicable): Removes common stop words to improve entity recognition accuracy.

### Entity Extraction

Entity extraction is performed using SpaCy's pre-trained models to identify key entities in the document text. The project focuses on detecting:

- **PERSON**: Names of individuals.
- **ID**: Identifiable codes such as passport numbers or national IDs.

This process involves tokenizing the text, identifying entities, and classifying each according to the predefined categories.

### Compliance Rule Checking

Compliance rules are defined in a JSON file (`compliance_rules.json`). These rules can be customized as needed. Examples of rules include:

- **Sensitive Information Rule**: Flags text containing specific patterns (e.g., ID numbers).
- **Prohibited Terms**: Checks for the presence of keywords or phrases that are considered non-compliant.

Each rule is applied sequentially, and any matches are logged as potential compliance issues.

### Confidential Information Detection

A machine learning model is used to detect confidential information. The model is trained on text samples containing confidential and non-confidential content, using a binary classification approach. The steps involved are:

1. **Training Data**: A set of labeled text samples indicating whether they contain confidential information.
2. **Model Training**: A simple classification model (e.g., logistic regression or SVM) trained on text features.
3. **Prediction**: The model predicts if a segment of text is likely confidential.

## Configuration and Customization

- **Compliance Rules**: Customize the `compliance_rules.json` file to define new rules or modify existing ones.
- **Entity Types**: If new entities are needed, modify the `analyze.py` file to include additional entity recognition.
- **Model Re-training**: If more accurate detection is required, update the training data and retrain the model using `train_confidential_model.py`.

## Model Training

To train the confidential information detection model, follow these steps:

1. **Prepare Training Data**: Ensure you have a labeled dataset in a CSV format with columns `text` and `label` (1 for confidential, 0 for non-confidential).
2. **Run Training Script**: Execute the `train_confidential_model.py` script to train the model. This will generate a `confidential_model.pkl` file.
3. **Evaluate Model**: Validate the model performance and adjust parameters as necessary.

## Extending the Project

1. **Add New Entities**: Modify `analyze.py` to add custom entity recognition patterns.
2. **Custom Compliance Rules**: Define new rules in `compliance_rules.json` and add corresponding logic in `rules.py`.
3. **Integrate External NLP Models**: Replace SpaCy with another NLP framework if specialized models are required.
4. **Enhance Confidential Detection Model**: Experiment with other machine learning or deep learning models by modifying `train_confidential_model.py`.

## Example Use Cases

- **Legal Compliance in Document Management**: Automatically check legal documents for compliance issues.
- **Data Privacy Audits**: Detect sensitive information in PDFs before sharing with third parties.
- **HR Documentation Review**: Ensure HR documents meet regulatory requirements for data protection.

## Troubleshooting

### Common Issues

1. **Model Loading Errors**: Ensure the `confidential_model.pkl` file exists in the expected directory.
2. **Missing SpaCy Model**: Run `python -m spacy download en_core_web_md` if SpaCy models are not found.
3. **Compliance Rule Errors**: Verify `compliance_rules.json` has correct JSON syntax.

### Debugging Tips

- Use `print` statements in code to verify data at various stages.
- Run individual functions in isolation to identify where issues arise.
