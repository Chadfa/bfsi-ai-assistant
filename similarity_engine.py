import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class SimilarityEngine:
    def __init__(self, dataset_path):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        with open(dataset_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.texts = [item["input"] for item in self.data]
        self.embeddings = self.model.encode(self.texts)

        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

    def search(self, query, threshold=0.6):
        query_embedding = self.model.encode([query])
        D, I = self.index.search(np.array(query_embedding), 1)

        score = D[0][0]
        index = I[0][0]

        if score < threshold:
            return self.data[index]["output"]

        return None
