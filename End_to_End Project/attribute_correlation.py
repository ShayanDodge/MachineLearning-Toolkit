import pandas as pd
import dataset_loader
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Loading the dataset
df = dataset_loader.load_data(dataset_loader.find_directory("datasets\housing\housing.csv"))

corr_matrix = df.drop('ocean_proximity', axis=1).corr()
print(corr_matrix["median_house_value"].sort_values(ascending=False))

attributes = ["median_house_value", "median_income", "total_rooms",
"housing_median_age"]
scatter_matrix(df[attributes], figsize=(12, 8),diagonal='kde')
plt.show()