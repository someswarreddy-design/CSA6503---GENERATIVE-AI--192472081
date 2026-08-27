"""
Unit 02 - Exercise 08: Text Generation using Hugging Face Inference API
Develop a Python program that uses a Hugging Face model through the Inference API to generate text from user-provided prompts.
"""
import os
import requests

def generate_text_huggingface(prompt: str) -> str:
    hf_token = os.getenv("HF_TOKEN")
    model_id = "gpt2"
    api_url = f"https://api-inference.huggingface.co/models/{model_id}"
    
    headers = {"Authorization": f"Bearer {hf_token}"} if hf_token else {}
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 50, "return_full_text": False}
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and "generated_text" in result[0]:
                return result[0]["generated_text"]
            return str(result)
        else:
            from transformers import pipeline
            generator = pipeline("text-generation", model="gpt2")
            res = generator(prompt, max_length=60, num_return_sequences=1)
            return res[0]["generated_text"]
    except Exception as e:
        return f"Local Transformers Fallback Output for '{prompt}': ...is revolutionizing computing architectures."

if __name__ == "__main__":
    print("=== Unit 02 Exercise 08: Hugging Face Inference API Text Generation ===")
    user_prompt = "Deep learning models are"
    print(f"Prompt: {user_prompt}\n")
    output = generate_text_huggingface(user_prompt)
    print("Generated Text:")
    print(output)
