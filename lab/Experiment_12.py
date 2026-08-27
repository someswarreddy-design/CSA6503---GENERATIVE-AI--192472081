"""
Experiment 12: Generating Contextual Embeddings with BERT
"""
import torch
from transformers import BertTokenizer, BertModel

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Input sentence
text = "Artificial Intelligence is transforming the world."

# Tokenize the input
inputs = tokenizer(text, return_tensors="pt")

# Generate contextual embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Get the last hidden state (embeddings)
embeddings = outputs.last_hidden_state

print("Text:", text)
print("Embeddings Shape:", embeddings.shape)
print("Contextual Embeddings:")
print(embeddings)
