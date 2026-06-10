import pandas as pd
import json
import os

df = pd.read_parquet('dataset/dataset.parquet')
df = df.dropna()
print(f"Total rows: {len(df)}")

os.makedirs('data', exist_ok=True)

def format_row(row):
    prompt = row['instruction'] if row['instruction'] else row['input']
    return {
        "messages": [
            {"role": "system", "content": "You are IlaAI, an expert agricultural assistant for Indian farmers. Answer clearly and helpfully about crops, diseases, farming practices, government schemes, and market prices."},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": row['output']}
        ]
    }

train = df.sample(frac=0.95, random_state=42)
valid = df.drop(train.index)

with open('data/train.jsonl', 'w') as f:
    for _, row in train.iterrows():
        f.write(json.dumps(format_row(row)) + '\n')

with open('data/valid.jsonl', 'w') as f:
    for _, row in valid.iterrows():
        f.write(json.dumps(format_row(row)) + '\n')

print(f"Train: {len(train)} rows")
print(f"Valid: {len(valid)} rows")
print("Done! ✅")
