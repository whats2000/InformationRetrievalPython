from typing import List, Dict

from BooleanRetrieval.inverted_index import InvertedIndex


def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by converting it to lowercase and stripping extra spaces.
    :param text: The input document as a string.
    :return: The preprocessed text as a string.
    """
    return text.lower().strip()


def generate_incidence_matrix(index: InvertedIndex, documents: Dict[str, str]) -> None:
    """
    Generate and display the term-document incidence matrix.

    :param index: The inverted index built from documents.
    :param documents: A dictionary of document IDs and their text content.
    :return: None
    """
    print("Term-Document Incidence Matrix:")

    # Get a sorted list of terms and documents for consistent display
    terms = sorted(index.index.keys())
    doc_ids = sorted(documents.keys())

    # Print the matrix header (document IDs)
    print(f"{'Term':<15} {' '.join(doc_ids)}")

    # Iterate through each term and check its presence in documents
    for term in terms:
        # Check if term exists in each document
        presence = [(doc_id in [d[0] for d in index.get_postings_list(term)]) for doc_id in doc_ids]
        # Print 1 for presence, 0 for absence
        row = ' '.join(['1' if p else '0' for p in presence])
        print(f"{term:<15} {row}")


def generate_inverted_index(index: InvertedIndex) -> None:
    """
    Generate and display the inverted index representation.

    :param index: The inverted index built from documents.
    :return: None
    """
    print("\nInverted Index Representation:")

    # Iterate through the sorted terms
    for term, postings in sorted(index.index.items()):
        doc_list = [doc_id for doc_id, _ in postings]
        print(f"{term} -> {doc_list}")


def boolean_and(term1: str, term2: str, index: InvertedIndex) -> List[str]:
    postings_term1 = set([doc_id for doc_id, _ in index.get_postings_list(term1)])
    postings_term2 = set([doc_id for doc_id, _ in index.get_postings_list(term2)])
    return list(postings_term1 & postings_term2)


def boolean_or(term1: str, term2: str, index: InvertedIndex) -> List[str]:
    postings_term1 = set([doc_id for doc_id, _ in index.get_postings_list(term1)])
    postings_term2 = set([doc_id for doc_id, _ in index.get_postings_list(term2)])
    return list(postings_term1 | postings_term2)


def boolean_not(term1: str, exclusion_set: List[str], index: InvertedIndex) -> List[str]:
    postings_term1 = set([doc_id for doc_id, _ in index.get_postings_list(term1)])
    return list(postings_term1 - set(exclusion_set))
