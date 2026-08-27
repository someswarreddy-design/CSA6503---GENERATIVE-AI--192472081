"""
Experiment 04: Pandas DataFrame Basics
"""
import pandas as pd

# Define sample student data
data = {
    "Name": ["Ram", "Sita", "John", "Anu"],
    "Grade": ["A", "B", "A+", "C"]
}

# Create and display DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)
