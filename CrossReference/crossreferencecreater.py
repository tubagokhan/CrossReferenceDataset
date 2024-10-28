import os
import json
import re
import csv
import unicodedata

# Import DOCUMENT_ID_MAP from document_id_map.py
from document_id_map import DOCUMENT_ID_MAP

# Directory containing JSON files
INPUT_DIRECTORY = "StructuredRegulatoryDocumentsJson"
OUTPUT_CSV = "cross_reference_dataset.csv"

# Regular expressions to extract various references
PART_PATTERN = re.compile(r'\bPart\s\d+', re.IGNORECASE)
SECTION_PATTERN = re.compile(r'\bSection\s\d+(\.\d+)*', re.IGNORECASE)
SUBSECTION_PATTERN = re.compile(r'subsection\s\d+(\([a-zA-Z0-9]+\))*', re.IGNORECASE)
RULE_PATTERN = re.compile(r'\bRule\s\d+(\.\d+)*(\([a-zA-Z0-9]+\))*', re.IGNORECASE)
CHAPTER_PATTERN = re.compile(r'\bChapter\s\d+(,\sRule\s\d+(\.\d+)*)?', re.IGNORECASE)
CATEGORY_PATTERN = re.compile(r'Category\s\d+[A-Z]*', re.IGNORECASE)
APP_SECTION_PATTERN = re.compile(r'APP\d+\.\w+\.\d+(\.\d+)*', re.IGNORECASE)
GUIDANCE_PATTERN = re.compile(r'Guidance(\.\d+)*', re.IGNORECASE)
GUIDANCE_NOTE_PATTERN = re.compile(r'Guidance\snote\s\d+', re.IGNORECASE)
IFRS_PATTERN = re.compile(r'International Financial Reporting Standards', re.IGNORECASE)
FEDERAL_LAW_PATTERN = re.compile(r'Federal Law No\. \d+ of \d+', re.IGNORECASE)
DECREE_PATTERN = re.compile(r'Federal Decree by Law No\. \d+ of \d+', re.IGNORECASE)
CABINET_DECISION_PATTERN = re.compile(r'Cabinet Decision No\. \(\d+\) of \d+', re.IGNORECASE)
INTERNATIONAL_STANDARD_PATTERN = re.compile(r'(FATF|Basel Committee|Wolfsberg Group|Network for Greening the Financial System)', re.IGNORECASE)
PARAGRAPH_PATTERN = re.compile(r'paragraph\s\d+\s+of\s+Chapter\s\d+', re.IGNORECASE)
SCHEDULE_PATTERN = re.compile(r'Chapter\s\d+\s+of\s+Schedule\s\d+\s+of\s+FSMR', re.IGNORECASE)
GEN_PATTERN = re.compile(r'GEN\s\d+\.\d+\.\d+', re.IGNORECASE)
FEES_PATTERN = re.compile(r'FEES\s\d+(\.\d+)*', re.IGNORECASE)
FUNDS_PATTERN = re.compile(r'FUNDS\sRules\s\d+\.\d+\.\d+\([a-z]\)', re.IGNORECASE)
SECTION_SUBSECTION_PATTERN = re.compile(r'(section|subsection|sub-paragraph)\s(\d+|\([a-zA-Z0-9]+\))(\s*to\s*\d+)?', re.IGNORECASE)
FSMR_PATTERN = re.compile(r'\bSection\s\d+\s+of\s+the\sFSMR', re.IGNORECASE)
MKT_RULE_PATTERN = re.compile(r'under\sMKT\sRule\s\d+(\.\d+)*(\([a-zA-Z0-9]+\))*', re.IGNORECASE)

# Fieldnames for the output CSV
FIELDNAMES = [
    "SourceDocumentName",
    "SourceID",
    "SourceDocumentID",
    "SourcePassageID",
    "SourcePassage",
    "SourceReferenceText",
    "ReferenceType",
    "TargetID",
    "TargetDocumentID",
    "TargetPassageID",
    "TargetPassage",
]

def count_words(text):
    """
    Counts the number of words in the given text.
    """
    return len(text.split())

def clean_passage_text(passage_text):
    """
    Removes text between '/Table Start' and '/Table End' in the passage.
    """
    # Remove text between '/Table Start' and '/Table End'
    cleaned_text = re.sub(r'/Table Start.*?/Table End', '', passage_text, flags=re.DOTALL)
    return cleaned_text

def extract_references(passage_text):
    """
    Extracts references from the given passage text using regex.
    """
    # Clean the passage text before extraction
    passage_text = clean_passage_text(passage_text)
    
    references = []

    # Match various patterns in the passage text
    part_references = PART_PATTERN.findall(passage_text)
    section_references = SECTION_PATTERN.findall(passage_text)
    subsection_references = SUBSECTION_PATTERN.findall(passage_text)
    rule_references = RULE_PATTERN.findall(passage_text)
    chapter_references = CHAPTER_PATTERN.findall(passage_text)
    category_references = CATEGORY_PATTERN.findall(passage_text)
    app_section_references = APP_SECTION_PATTERN.findall(passage_text)
    guidance_references = GUIDANCE_PATTERN.findall(passage_text)
    guidance_note_references = GUIDANCE_NOTE_PATTERN.findall(passage_text)
    ifrs_references = IFRS_PATTERN.findall(passage_text)
    federal_law_references = FEDERAL_LAW_PATTERN.findall(passage_text)
    decree_references = DECREE_PATTERN.findall(passage_text)
    cabinet_decision_references = CABINET_DECISION_PATTERN.findall(passage_text)
    international_standard_references = INTERNATIONAL_STANDARD_PATTERN.findall(passage_text)
    paragraph_references = PARAGRAPH_PATTERN.findall(passage_text)
    schedule_references = SCHEDULE_PATTERN.findall(passage_text)
    gen_references = GEN_PATTERN.findall(passage_text)
    fees_references = FEES_PATTERN.findall(passage_text)
    funds_references = FUNDS_PATTERN.findall(passage_text)
    section_subsection_references = SECTION_SUBSECTION_PATTERN.findall(passage_text)
    fsmr_references = FSMR_PATTERN.findall(passage_text)
    mkt_rule_references = MKT_RULE_PATTERN.findall(passage_text)

    # Append extracted references to the list, ensuring meaningful information is retained
    references.extend([ref.strip() for ref in part_references if ref.strip()])
    references.extend([ref.strip() for ref in section_references if ref.strip()])
    references.extend([f"subsection {ref.strip()}" for ref in subsection_references if ref.strip()])
    references.extend([f"Rule {ref[0].strip()}" for ref in rule_references if ref[0].strip()])
    references.extend([f"{' '.join(filter(None, ref)).strip()}" for ref in chapter_references if any(ref)])
    references.extend([ref.strip() for ref in category_references if ref.strip()])
    references.extend([ref.strip() for ref in app_section_references if ref.strip()])
    references.extend([f"Guidance {ref.strip()}" for ref in guidance_references if ref.strip()])
    references.extend([ref.strip() for ref in guidance_note_references if ref.strip()])
    references.extend([ref.strip() for ref in ifrs_references if ref.strip()])
    references.extend([ref.strip() for ref in federal_law_references if ref.strip()])
    references.extend([ref.strip() for ref in decree_references if ref.strip()])
    references.extend([ref.strip() for ref in cabinet_decision_references if ref.strip()])
    references.extend([ref.strip() for ref in international_standard_references if ref.strip()])
    references.extend([ref.strip() for ref in paragraph_references if ref.strip()])
    references.extend([ref.strip() for ref in schedule_references if ref.strip()])
    references.extend([ref.strip() for ref in gen_references if ref.strip()])
    references.extend([f"FEES {ref.strip()}" for ref in fees_references if ref.strip()])
    references.extend([ref.strip() for ref in funds_references if ref.strip()])
    references.extend([f"{ref[0].strip()} {ref[1].strip()}" + (f" to {ref[2].strip()}" if ref[2] else "") for ref in section_subsection_references if ref[0].strip() and ref[1].strip()])
    references.extend([ref.strip() for ref in fsmr_references if ref.strip()])
    references.extend([f"{' '.join(filter(None, ref)).strip()}" for ref in mkt_rule_references if any(ref)])

    return references

def normalize_unicode(text):
    """
    Normalize unicode characters in the given text.
    """
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

def main():
    # List to store rows for the CSV
    csv_rows = []
    documents = {}

    # Load all documents into memory
    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".json"):
            filepath = os.path.join(INPUT_DIRECTORY, filename)
            with open(filepath, "r", encoding="utf-8") as json_file:
                document = json.load(json_file)
                if document:
                    document_id = document[0].get("DocumentID")
                    documents[document_id] = {"DocumentName": filename, "Items": document}

    # Iterate through each document
    for document_id, doc_content in documents.items():
        document = doc_content.get("Items", [])
        document_name_list = DOCUMENT_ID_MAP.get(document_id, ["Unknown"])
        document_name = document_name_list[0]

        # Iterate through each item in the JSON document
        for item in document:
            source_id = item.get("ID")
            source_document_id = item.get("DocumentID")
            source_passage_id = item.get("PassageID")
            source_passage = item.get("Passage", "")

            # Skip passage if it exceeds 200 words
            if count_words(source_passage) > 200:
                continue

            # Extract references from the passage text
            references = extract_references(source_passage)

            # Normalize the passage text to remove unicode characters
            source_passage = normalize_unicode(source_passage)

            if references:
                for ref in references:
                    
                    # Determine ReferenceType based on the presence of ‎
                    reference_type = "Internal" if "\u200e" in source_passage else ""
                    # Normalize the reference text
                    ref = normalize_unicode(ref)
                    # Append a new row to the CSV data
                    csv_rows.append({
                        "SourceDocumentName": document_name,
                        "SourceID": source_id,
                        "SourceDocumentID": source_document_id,
                        "SourcePassageID": source_passage_id,
                        "SourcePassage": source_passage,
                        "SourceReferenceText": ref,
                        "ReferenceType": reference_type,
                        "TargetID": "",
                        "TargetDocumentID": "",
                        "TargetPassageID": "",
                        "TargetPassage": "",
                    })

    # Write the extracted references to the CSV file
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(csv_rows)

if __name__ == "__main__":
    main()
