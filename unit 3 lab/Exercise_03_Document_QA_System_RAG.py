"""
Unit 03 - Exercise 03: Document Question Answering using Retrieval-Augmented Generation (RAG)
Develop a document Question Answering system using Retrieval-Augmented Generation (RAG).
"""

class RAGDocumentQA:
    def __init__(self):
        self.documents = [
            "Retrieval-Augmented Generation (RAG) combines dense vector retrieval with large language models.",
            "RAG prevents LLM hallucinations by grounding responses in retrieved source documents.",
            "Vector databases store high-dimensional embeddings generated from text chunks for fast similarity lookup."
        ]
        
    def retrieve(self, query: str) -> str:
        # Simple TF-IDF / Keyword match retrieval
        query_words = set(query.lower().split())
        best_doc = self.documents[0]
        max_overlap = 0
        for doc in self.documents:
            overlap = len(query_words.intersection(set(doc.lower().split())))
            if overlap > max_overlap:
                max_overlap = overlap
                best_doc = doc
        return best_doc
        
    def generate_answer(self, query: str) -> str:
        retrieved_context = self.retrieve(query)
        prompt = (
            f"[SYSTEM CONTEXT]: {retrieved_context}\n"
            f"[USER QUESTION]: {query}\n"
            f"[RAG ANSWER]: Based on the retrieved documentation, " + retrieved_context
        )
        return prompt

if __name__ == "__main__":
    print("=== Unit 03 Exercise 03: Document QA System using RAG ===")
    rag_system = RAGDocumentQA()
    
    question = "How does RAG prevent hallucinations in LLMs?"
    print(f"User Question: '{question}'\n")
    
    rag_response = rag_system.generate_answer(question)
    print(rag_response)
