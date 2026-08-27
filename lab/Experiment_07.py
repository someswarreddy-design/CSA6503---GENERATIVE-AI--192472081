"""
Experiment 07: Sentiment Analysis with HuggingFace Pipeline
"""
from transformers import pipeline

# Load pre-trained DistilBERT sentiment classifier
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

sentence = "I love Python"
result = classifier(sentence)

print("Input Text:", sentence)
print("Sentiment Analysis Result:", result)
