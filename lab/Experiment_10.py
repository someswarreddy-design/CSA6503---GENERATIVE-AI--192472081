"""
Experiment 10: HuggingFace Pipeline Sentiment Analysis
"""
from transformers import pipeline

# Initialize default sentiment analysis pipeline
pipe = pipeline("sentiment-analysis")

text = "Python is very easy to learn."
result = pipe(text)

print("Input Text:", text)
print("Pipeline Output:", result)
