"""
Unit 02 - Exercise 07: Text Generation using Google Gemini LLM API
Develop a Python program using the Gemini API to generate responses for different user prompts and display the generated output.
"""
import os

def generate_text_gemini(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if api_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Gemini API Error: {e}"
    else:
        return (
            f"[DEMO MODE - GEMINI API KEY NOT DETECTED]\n"
            f"Prompt: '{prompt}'\n"
            f"Gemini Response: Google Gemini multimodal models process complex text, code, and visual prompts "
            f"with high accuracy using sparse attention transformers."
        )

if __name__ == "__main__":
    print("=== Unit 02 Exercise 07: Google Gemini LLM API Text Generation ===")
    prompts = [
        "What are transformers in Machine Learning?",
        "Write a 2-sentence summary of neural networks."
    ]
    for i, p in enumerate(prompts, 1):
        print(f"\n--- Prompt {i}: {p} ---")
        output = generate_text_gemini(p)
        print(output)
