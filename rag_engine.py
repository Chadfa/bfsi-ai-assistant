import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class RAGEngine:
    def __init__(self, docs_path):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        with open(docs_path, "r", encoding="utf-8") as f:
            text = f.read()

        self.docs = text.split("\n\n")

        self.embeddings = self.model.encode(self.docs)

        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

    def retrieve(self, query, top_k=1):
        query_embedding = self.model.encode([query])
        D, I = self.index.search(np.array(query_embedding), top_k)

        return [self.docs[i] for i in I[0]]
