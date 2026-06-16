import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
if not filename.endswith('.csv'):
    filename += '.csv'

df = pd.DataFrame({"id": [1, 2, 3], "score": [85, 92, 78]})
df.to_csv(filename, index=False)

print(f"Data written to {filename}")