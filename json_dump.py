import pandas as pd

old = pd.read_csv('cse.csv')

with open("cse.json", "w") as f:
    old.to_json(f)