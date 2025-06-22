# /export_model.py
import pandas as pd, json, shutil, os

df = pd.read_csv("data/processed/dataset.csv")
corr = dict(zip(df["noisy"], df["correct"]))
os.makedirs("deploy", exist_ok=True)
with open("deploy/corrections.json","w",encoding="utf-8") as f:
    json.dump(corr, f, ensure_ascii=False, indent=2)
shutil.copy("model/model.keras", "deploy/model.keras")
shutil.copy("model/tokenizer/tokenizer.json", "deploy/tokenizer.json")
