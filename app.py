from similarity_engine import SimilarityEngine
from rag_engine import RAGEngine
from guardrails import is_out_of_domain, contains_sensitive_data
from slm_engine import SLMEngine


sim_engine = SimilarityEngine("dataset/bfsi_alpaca.json")
rag_engine = RAGEngine("rag/knowledge_docs.txt")
slm_engine = SLMEngine()


def get_response(query):
    # Guardrail check
    if is_out_of_domain(query):
        return "I'm sorry, I can only assist with banking and financial service related queries."
    
    if contains_sensitive_data(query):
        return "For security reasons, we cannot process sensitive personal information. Please contact customer support."


    # Tier 1 - Dataset match
    response = sim_engine.search(query)
    if response:
        return response

    # Tier 2 — Lightweight SLM
    slm_response = slm_engine.generate(query)
    if slm_response:
        return slm_response
    
    # Tier 3 - RAG fallback
    retrieved_docs = rag_engine.retrieve(query)
    return f"Based on our internal policy documentation:\n\n{retrieved_docs[0]}\n\nFor exact figures or account-specific details, please refer to your loan agreement or contact support."


if __name__ == "__main__":
    print("BFSI AI Assistant Ready. Type 'exit' to quit.\n")

    while True:
        user_query = input("User: ")

        if user_query.lower() == "exit":
            break

        reply = get_response(user_query)
        print("\nAssistant:", reply, "\n")
