"""
Unit 02 - Exercise 06: Text Generation using OpenAI LLM API
Develop a Python program to connect to an LLM using the OpenAI API and generate text based on a user-provided prompt.
"""
import os

def generate_text_openai(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            import openai
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"OpenAI API Call Error: {e}"
    else:
        # Fallback / Offline Demo Mode
        return (
            f"[DEMO MODE - OPENAI API KEY NOT DETECTED]\n"
            f"Prompt received: '{prompt}'\n"
            f"Generated Output: Artificial Intelligence and LLMs transform text generation "
            f"by processing semantic context and predicting optimal sequential word distributions."
        )

if __name__ == "__main__":
    print("=== Unit 02 Exercise 06: OpenAI LLM Text Generation ===")
    user_prompt = "Explain the importance of Generative AI in modern engineering."
    print(f"User Prompt: {user_prompt}\n")
    result = generate_text_openai(user_prompt)
    print("Generated Text Output:")
    print(result)
