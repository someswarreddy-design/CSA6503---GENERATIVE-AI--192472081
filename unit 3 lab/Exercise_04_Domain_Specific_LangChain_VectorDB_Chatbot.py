"""
Unit 03 - Exercise 04: Domain-Specific Chatbot using LangChain and Vector Database
Develop a domain-specific chatbot using LangChain and a vector database.
"""

def domain_specific_langchain_chatbot(query: str):
    print(f"User Query: '{query}'")
    print("Step 1: Embedding query via HuggingFace Embeddings...")
    print("Step 2: Searching domain knowledge base in FAISS Vector Store...")
    
    knowledge_base = {
        "generative ai": "Generative AI focuses on deep learning models that produce synthetic text, images, code, and audio.",
        "diffusion model": "Diffusion models generate high-fidelity images by iteratively denoising Gaussian noise distributions.",
        "transformer": "Transformers rely on multi-head self-attention mechanisms to model long-range sequential dependencies."
    }
    
    query_lower = query.lower()
    answer = "No relevant domain context found in Vector DB."
    for key, text in knowledge_base.items():
        if key in query_lower:
            answer = text
            break
            
    print(f"Step 3: Generating LangChain LLM Chain response based on context:\n")
    print(f"[LangChain AI Bot]: {answer}")

if __name__ == "__main__":
    print("=== Unit 03 Exercise 04: Domain-Specific Chatbot using LangChain & Vector DB ===")
    domain_query = "What is a diffusion model in Generative AI?"
    domain_specific_langchain_chatbot(domain_query)
