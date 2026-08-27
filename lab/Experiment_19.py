"""
Experiment 19: Text Completion using GPT-2 Pipeline
"""
from transformers import pipeline

# Load pre-trained GPT-2 model
generator = pipeline("text-generation", model="gpt2")

prompt = "Technology will"
result = generator(prompt, max_length=40)

print("Prompt:", prompt)
print("Generated Text:")
print(result[0]["generated_text"])
