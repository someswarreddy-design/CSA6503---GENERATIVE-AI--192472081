"""
Experiment 08: BERT Tokenizer Tokenization
"""
from transformers import BertTokenizer

# Load the pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

text = "Artificial Intelligence is amazing."
tokens = tokenizer.tokenize(text)

print("Input Text:", text)
print("Tokens:", tokens)
