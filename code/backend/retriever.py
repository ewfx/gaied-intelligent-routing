import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.documents = []
        self.metadata = []

    def add_document(self, text, type_label, sub_type_label):
        embedding = self.model.encode([text])[0]
        self.index.add(np.array([embedding]).astype('float32'))
        self.documents.append(text)
        self.metadata.append({"type": type_label, "sub_type": sub_type_label})

    def retrieve_similar(self, query, top_k=2):
        query_embedding = self.model.encode([query])[0]
        D, I = self.index.search(np.array([query_embedding]).astype('float32'), top_k)

        retrieved_data = []
        for idx in I[0]:
            if idx < len(self.documents):
                retrieved_data.append({
                    "text": self.documents[idx],
                    "type": self.metadata[idx]["type"],
                    "sub_type": self.metadata[idx]["sub_type"]
                })
        return retrieved_data
