import pandas as pd
from dataset_spliter_sklearn import*

df_cat = df[["ocean_proximity"]]
df_cat.head(50)

#%% OrdinalEncoder method
# from sklearn.preprocessing import OrdinalEncoder
# ordinal_encoder = OrdinalEncoder()
# df_cat_encoded = ordinal_encoder.fit_transform(df_cat)
# df_cat_encoded[:500]
# print(ordinal_encoder.categories_)

#%% OneHotEncoder method
from sklearn.preprocessing import OneHotEncoder
cat_encoder = OneHotEncoder()
df_cat_1hot = cat_encoder.fit_transform(df_cat)
print(df_cat_1hot.toarray())