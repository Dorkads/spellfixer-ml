import pandas as pd, json
df = pd.read_csv("data/processed/dataset.csv")
corr = dict(zip(df["noisy"], df["correct"]))
json.dump(corr, open("../spellfixer-backend/corrections.json","w"), ensure_ascii=False, indent=2)
