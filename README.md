# Compliance Analysis Project

## Overview

The Compliance Analysis Project is a tool designed to help organizations manage compliance risks in PDF documents. It uses a combination of Natural Language Processing (NLP), predefined compliance rules, and stakeholder information extraction to analyze document contents for confidential information, stakeholder IDs, passport numbers, and potential compliance violations.

## Features

- **Entity Extraction**: Identifies stakeholder names, IDs, and passport numbers.
- **Compliance Rule Checking**: Analyzes text against predefined compliance rules.
- **Confidential Information Detection**: Uses a machine learning model to detect confidential data.
- **PDF Metadata Extraction**: Extracts metadata from PDF documents.

## Directory Structure

```plaintext
compliance_project/
├── compliance_output.json          # Output from a compliance analysis
├── compliance_rules.json           # JSON file defining compliance rules
├── confidential_model.pkl          # Machine learning model for confidential data detection
├── output.json                     # Sample output data
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
├── sample_doc.pdf                  # Sample PDF document for testing
└── src/
    └── compliance_project/
        ├── __init__.py
        ├── analyze.py              # Entity extraction functions
        ├── confidential_data.py    # Confidential data detection model training
        ├── extract_stakeholder_info.py # Stakeholder info extraction function
        ├── main.py                 # Main script for running compliance analysis
        ├── preprocess.py           # PDF text extraction and preprocessing
        ├── rules.py                # Compliance rule checking functions
        └── train_confidential_model.py # Script for training confidential data detection model


## Installation

To set up the project environment, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/MoncaDaniel/compliance_project.git
    cd compliance_project
    ```

2. **Create a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Download the SpaCy model**:

    ```bash
    python -m spacy download en_core_web_md
    ```

## Usage

Run the compliance analysis by executing the main script with a PDF file:

```bash
python src/compliance_project/main.py <file_path> [output_path]
# Project Modules

1. **`preprocess.py`**  
   Contains functions to load and preprocess PDF documents.

2. **`analyze.py`**  
   Includes functions for named entity recognition (NER) using SpaCy.

3. **`rules.py`**  
   Contains rule-based compliance checking functions.

4. **`extract_stakeholder_info.py`**  
   Extracts stakeholder names and ID numbers from document text.

5. **`train_confidential_model.py`**  
   Trains a machine learning model for confidential data detection.

# Extending the Project

To add new compliance rules or customize entity recognition, modify the `rules.py` or `analyze.py` files as needed. Update `requirements.txt` if adding new dependencies.

# License

This project is licensed under the MIT License.
