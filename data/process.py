import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle

data = pd.read_csv("data/D2_combined_gene_dep_scores.csv", index_col=0)
gene_map = {i: j for i, j in zip(range(data.shape[0]), data.index)}
cancer_map = {i: j for i, j in zip(range(data.shape[1]), data.columns)}

with open("data/cancer_map.pkl", "wb") as f:
    pickle.dump(cancer_map, f)

