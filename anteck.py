import pandas as pd
import numpy as np

df = pd.read_csv("kickstarter.csv")
print(df.to_string())

print(df["status"] .replace("\\N", np.nan, regex=False))