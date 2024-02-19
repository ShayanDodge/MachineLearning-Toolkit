import pandas as pd
from dataset_spliter_sklearn import*


df = strat_train_set.drop("median_house_value", axis=1)
df_labels = strat_train_set["median_house_value"].copy()