"""
Experiment 39: Vector Database and QA RAG Bot with FAISS and HuggingFace Embeddings
"""
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# 1. Domain-specific documents
documents = [
    "Python variables store values in memory.",
    "Python lists are ordered and mutable collections.",
    "Python tuples are ordered and immutable collections.",
    "Python dictionaries store data using key-value pairs.",
    "Python functions are reusable blocks of code.",
    "Python loops are used to repeat a block of code.",
    "Python if statements are used for decision making."
]

# 2. Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 3. Create vector database
vector_db = FAISS.from_texts(
    documents,
    embeddings
)

print("Python knowledge base created successfully.")

# 4. Interactive Chatbot Loop
if __name__ == "__main__":
    while True:
        try:
            question = input("\nYou: ")
            if question.lower() == "exit":
                print("Chatbot: Goodbye!")
                break

            results = vector_db.similarity_search(question, k=2)
            print("\nChatbot:")
            for result in results:
                print("-", result.page_content)
        except (EOFError, KeyboardInterrupt):
            break
