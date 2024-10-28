import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import statistics

# Path to the input CSV file
INPUT_CSV = "cross_reference_dataset.csv"

# Function to analyze the reference count per document
def analyze_references(input_csv):
    reference_count = defaultdict(int)
    total_documents = 40

    # Read the CSV file
    with open(input_csv, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        # Iterate over each row and count references per document
        for row in reader:
            document_id = int(row["SourceDocumentID"])
            reference_count[document_id] += 1

    # Sort the reference count by document ID
    sorted_reference_count = dict(sorted(reference_count.items()))

    # Print the reference count per document
    for document in range(1, total_documents + 1):
        count = sorted_reference_count.get(document, 0)
        print(f"Document ID: {document}, Reference Count: {count}")

    # Print documents that do not include any references
    documents_without_references = [doc_id for doc_id in range(1, total_documents + 1) if doc_id not in reference_count]
    if documents_without_references:
        print("\nDocuments without any references:")
        for doc_id in documents_without_references:
            print(f"Document ID: {doc_id}")

    # Summary statistics
    reference_counts = [sorted_reference_count.get(doc_id, 0) for doc_id in range(1, total_documents + 1)]
    total_references = sum(reference_counts)
    average_references = statistics.mean(reference_counts)
    median_references = statistics.median(reference_counts)
    min_references = min(reference_counts)
    max_references = max(reference_counts)

    print("\nSummary Statistics:")
    print(f"Total References: {total_references}")
    print(f"Average References per Document: {average_references:.2f}")
    print(f"Median References per Document: {median_references}")
    print(f"Minimum References in a Document: {min_references}")
    print(f"Maximum References in a Document: {max_references}")

    # Percentage of documents with references
    documents_with_references = total_documents - len(documents_without_references)
    percentage_with_references = (documents_with_references / total_documents) * 100
    print(f"\nPercentage of Documents with References: {percentage_with_references:.2f}%")

    # Plot the reference count per document
    document_ids = list(range(1, total_documents + 1))
    plt.figure(figsize=(10, 6))
    plt.bar(document_ids, reference_counts, color='skyblue')
    plt.xlabel('Document ID')
    plt.ylabel('Reference Count')
    plt.title('Reference Count per Document')
    plt.xticks(document_ids)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Plot the distribution of reference counts
    plt.figure(figsize=(10, 6))
    plt.hist(reference_counts, bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Reference Count')
    plt.ylabel('Number of Documents')
    plt.title('Distribution of Reference Counts Across Documents')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    analyze_references(INPUT_CSV)
