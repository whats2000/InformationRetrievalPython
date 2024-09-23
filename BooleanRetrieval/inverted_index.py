from typing import Dict, List, Tuple

class InvertedIndex:
    def __init__(self) -> None:
        """
        Initialize the inverted index with an empty dictionary.
        """
        self.index: Dict[str, List[Tuple[str, int]]] = {}

    def add_document(self, doc_id: str, text: str) -> None:
        """
        Add a document to the inverted index and update term frequencies.

        :param doc_id: The ID of the document.
        :param text: The content of the document.
        :return: None
        """
        terms = text.split()
        term_dist: Dict[str, int] = {}

        # Calculate term frequency
        for term in terms:
            term = term.lower()
            if term not in term_dist:
                term_dist[term] = 0
            term_dist[term] += 1

        # Add to the inverted index
        for term, freq in term_dist.items():
            if term not in self.index:
                self.index[term] = []
            self.index[term].append((doc_id, freq))

    def sort_and_group(self) -> Dict[str, List[Tuple[str, int]]]:
        """
        Sort the terms in the inverted index alphabetically and group by term.

        :return: A sorted dictionary of terms and their posting lists.
        """
        sorted_index = dict(sorted(self.index.items()))
        return sorted_index

    def get_postings_list(self, term: str) -> List[Tuple[str, int]]:
        """
        Retrieve the posting list for a specific term.

        :param term: The term to look up.
        :return: A list of tuples containing document IDs and term frequencies.
        """
        return self.index.get(term.lower(), [])

    def generate_incidence_matrix(self, documents: Dict[str, str]) -> None:
        """
        Generate and display the term-document incidence matrix.

        :param documents: A dictionary of document IDs and their text content.
        :return: None
        """
        print("Term-Document Incidence Matrix:")

        # Get a sorted list of terms and documents for consistent display
        terms = sorted(self.index.keys())
        doc_ids = sorted(documents.keys())

        # Print the matrix header (document IDs)
        print(f"{'Term':<15} {' '.join(doc_ids)}")

        # Iterate through each term and check its presence in documents
        for term in terms:
            # Check if term exists in each document
            presence = [(doc_id in [d[0] for d in self.get_postings_list(term)]) for doc_id in doc_ids]
            # Print 1 for presence, 0 for absence
            row = ' '.join(['1' if p else '0' for p in presence])
            print(f"{term:<15} {row}")

    def generate_inverted_index(self) -> None:
        """
        Generate and display the inverted index representation.
        :return: None
        """
        print("\nInverted Index Representation:")

        # Iterate through the sorted terms
        for term, postings in sorted(self.index.items()):
            doc_list = [doc_id for doc_id, _ in postings]
            print(f"{term} -> {doc_list}")

    def boolean_and(self, term1: str, term2: str) -> List[str]:
        """
        Perform a boolean AND operation on two terms.
        :param term1: The first term.
        :param term2: The second term.
        :return: A list of document IDs that contain both terms.
        """
        postings_term1 = set([doc_id for doc_id, _ in self.get_postings_list(term1)])
        postings_term2 = set([doc_id for doc_id, _ in self.get_postings_list(term2)])
        return list(postings_term1 & postings_term2)

    def boolean_or(self, term1: str, term2: str) -> List[str]:
        """
        Perform a boolean OR operation on two terms.
        :param term1: The first term.
        :param term2: The second term.
        :return: A list of document IDs that contain either term.
        """
        postings_term1 = set([doc_id for doc_id, _ in self.get_postings_list(term1)])
        postings_term2 = set([doc_id for doc_id, _ in self.get_postings_list(term2)])
        return list(postings_term1 | postings_term2)

    def boolean_not(self, term1: str, exclusion_set: List[str]) -> List[str]:
        """
        Perform a boolean NOT operation on a term.
        :param term1: The term to exclude.
        :param exclusion_set: A list of document IDs to exclude.
        :return: A list of document IDs that contain the term but not in the exclusion set.
        """
        postings_term1 = set([doc_id for doc_id, _ in self.get_postings_list(term1)])
        return list(postings_term1 - set(exclusion_set))