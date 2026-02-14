from rag_engine import RAGEngine

rag = RAGEngine("rag/knowledge_docs.txt")

query = "How is EMI calculated?"

docs = rag.retrieve(query)

print("Query:", query)
print("Retrieved Document:\n")
print(docs[0])
