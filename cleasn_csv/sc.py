import pandas as pd
import numpy as np

df = pd.read_csv("trainingpeaks_coaches.csv")

# Name + Profile ko base maan ke duplicate hata do
df = df.drop_duplicates(subset=["Name", "Profile"])
df.index = np.arange(1,len(df)+1)

df.to_csv("ny.csv", index=True)
