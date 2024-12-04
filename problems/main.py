import os
from tools import process as p

# Define the directories
raw_dir = './raw_texts'
processed_dir = './processed_texts'

# Ensure the processed directory exists
os.makedirs(processed_dir, exist_ok=True)

# Iterate over all files in the raw directory
for filename in os.listdir(raw_dir):
    if filename.endswith(".txt"):
        # Read the raw file
        file_path = os.path.join(raw_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            raw = f.read()
        
        # Preprocess the content
        processed_text = p.process(raw)
        
        # Save the processed text to the corresponding file in the processed directory
        processed_file_path = os.path.join(processed_dir, filename)
        with open(processed_file_path, 'w', encoding='utf-8') as f:
            f.write(processed_text)

        print(f"Processed and saved: {filename}")
