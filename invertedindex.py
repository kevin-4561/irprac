import nltk
nltk.download('stopwords')
nltk.download('punkt')
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class SimpleSearchEngine:
    def __init__(self):
        self.inverted_index = defaultdict(list)
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def index_document(self, doc_id, document):
        words = [self.stemmer.stem(word.lower()) for word in word_tokenize(document) if word.isalnum() and word not in self.stop_words]
        for word in set(words):  # Using set to ensure unique terms in a document
            self.inverted_index[word].append(doc_id)

    def print_inverted_index(self):
        print("Inverted Index:")
        for term, doc_ids in self.inverted_index.items():
            print(f"{term}: {doc_ids}")

    def search(self, query):
        query_terms = set([self.stemmer.stem(term.lower()) for term in word_tokenize(query) if term.isalnum() and term not in self.stop_words])
        relevant_docs = set()
        for term in query_terms:
            relevant_docs.update(self.inverted_index.get(term, []))
        return relevant_docs

# Example usage:
search_engine = SimpleSearchEngine()

# Indexing documents
search_engine.index_document(1, "This is a sample document about python.")
search_engine.index_document(2, "Python programming language is widely used.")
search_engine.index_document(3, "Document indexing and retrieval is important in information retrieval.")

# Print the inverted index
search_engine.print_inverted_index()

# Prompt user for a search query
user_query = input("\nEnter your search query: ")
result = search_engine.search(user_query)

print("\nRelevant Documents:", result)
