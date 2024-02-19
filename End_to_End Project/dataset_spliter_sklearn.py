import matplotlib.pyplot as ply
import numpy as np
import pandas as pd
import dataset_loader

# Loading the dataset
df = dataset_loader.load_data(dataset_loader.find_directory("datasets\housing\housing.csv"))

# The simplest Scikit-Learn function to split datasets into multiple subsets
#  is train_test_split()
# from sklearn.model_selection import train_test_split
# train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

# Binning or grouping continuous data into discrete intervals, or bins. 
df["income_cat"] = pd.cut(df["median_income"],
bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
labels=[1, 2, 3, 4, 5])
# df["income_cat"].hist()
# ply.show()

# Creating a stratified train-test split based
# For this you can use Scikit-Learn’s StratifiedShuffleSplit class:
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
split.split(df, df["income_cat"])
for train_index, test_index in split.split(df, df["income_cat"]):
    strat_train_set = df.loc[train_index]
    strat_test_set = df.loc[test_index]
print(strat_test_set["income_cat"].value_counts() / len(strat_test_set))


