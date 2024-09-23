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

        :return: A sorted dictionary of terms and their postings lists.
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
