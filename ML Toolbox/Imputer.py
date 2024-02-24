import pandas as pd
from spliter_sklearn import*

# Splitting labels and predictions
df = strat_train_set.drop("median_house_value", axis=1)
df_labels = strat_train_set["median_house_value"].copy()

# Handling missing data manually
# df.dropna(subset=["total_bedrooms"]) # option 1
# df.drop("total_bedrooms", axis=1) # option 2
# median = df["total_bedrooms"].median() # option 3
# df["total_bedrooms"].fillna(median, inplace=True)

# Handling missing data using sklearn
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")
df_num = df.drop("ocean_proximity", axis=1)
imputer.fit(df_num)
imputer.statistics_
X = imputer.transform(df_num)
# The result is a plain NumPy array containing the transformed features. If you
# want to put it back into a pandas DataFrame, it’s simple:
housing_tr = pd.DataFrame(X, columns=df_num.columns,index=df_num.index)
