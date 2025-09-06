import pandas as pd

# load raw data
df = pd.read_csv("data/raw/School_dropout_Dataset.csv")

# normalize column names (remove spaces, replace % etc.)
df.columns = [c.strip().replace(" ", "_").replace("%", "pct") for c in df.columns]

# save processed copy
df.to_csv("data/processed/School_dropout_processed.csv", index=False)

print("Data cleaned & saved to data/processed/")
