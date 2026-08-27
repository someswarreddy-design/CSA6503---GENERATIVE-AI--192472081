"""
Unit 03 - Exercise 05: Simple AI Assistant Answering Questions using External Documents
Develop a simple AI assistant capable of answering questions using external documents.
"""
import os

def ai_assistant_load_and_answer(document_path: str, user_question: str) -> str:
    print(f"Loading External Document: '{document_path}'...")
    if not os.path.exists(document_path):
        # Create sample external doc if not present
        with open(document_path, "w", encoding="utf-8") as f:
            f.write(
                "Project Alpha Technical Manual:
"
                "1. Operating Temperature Range: -40 deg C to 85 deg C.
"
                "2. Input Voltage Requirement: 12V DC nominal (9V-18V range).
"
                "3. Firmware Recovery: Hold RESET button for 10 seconds during power cycle."
            )
            
    with open(document_path, "r", encoding="utf-8") as f:
        doc_content = f.read()
        
    print(f"External Document Loaded ({len(doc_content)} characters).\n")
    print(f"User Question: '{user_question}'")
    
    # Extract line matching query
    matching_lines = []
    for line in doc_content.splitlines():
        if any(term in line.lower() for term in user_question.lower().split()):
            matching_lines.append(line.strip())
            
    if matching_lines:
        extracted = " ".join(matching_lines)
        return f"[AI Assistant]: According to '{os.path.basename(document_path)}': {extracted}"
    return f"[AI Assistant]: The document '{os.path.basename(document_path)}' was searched, but no specific match was found."

if __name__ == "__main__":
    print("=== Unit 03 Exercise 05: AI Assistant using External Documents ===")
    ext_doc = os.path.join(root_dir, "Unit_03", "external_manual.txt")
    question = "What is the input voltage requirement?"
    
    response = ai_assistant_load_and_answer(ext_doc, question)
    print(f"\n{response}")
