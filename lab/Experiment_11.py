"""
Experiment 11: Tokenizing Text with BERT Tokenizer
"""
from transformers import BertTokenizer

# Load pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Input sentence
sentence = "Artificial Intelligence is transforming the world."

# Tokenize the sentence
tokens = tokenizer.tokenize(sentence)

# Display the tokens
print("Sentence:", sentence)
print("Tokens:", tokens)
