import pandas as pd
import dataset_loader

# Loading the dataset
df = dataset_loader.load_data(dataset_loader.find_directory("datasets\housing\housing.csv"))


df["rooms_per_household"] = df["total_rooms"]/df["households"]
df["bedrooms_per_room"] = df["total_bedrooms"]/df["total_rooms"]
df["population_per_household"] = df["population"]/df["households"]

corr_matrix = df.drop('ocean_proximity', axis=1).corr()
print(corr_matrix["median_house_value"].sort_values(ascending=False))