"""
Experiment 17: Generating Contextual Embeddings using BERT Model
"""
import torch
from transformers import BertTokenizer, BertModel

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Input sentence
sentence = "Artificial Intelligence is transforming the world."

# Tokenize the sentence
inputs = tokenizer(sentence, return_tensors="pt")

# Generate contextual embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Get the contextual embeddings
embeddings = outputs.last_hidden_state

# Display results
print("Sentence:", sentence)
print("Embedding Shape:", embeddings.shape)
print("Contextual Embeddings:")
print(embeddings)
