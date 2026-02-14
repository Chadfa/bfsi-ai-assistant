from similarity_engine import SimilarityEngine

engine = SimilarityEngine("dataset/bfsi_alpaca.json")

query = "Can I get a personal loan?"

response = engine.search(query)

print("Query:", query)
print("Response:", response)
