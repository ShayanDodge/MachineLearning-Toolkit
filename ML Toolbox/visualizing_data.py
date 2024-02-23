import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataset_loader

# Loading the dataset
df = dataset_loader.load_data(dataset_loader.find_directory("datasets\housing\housing.csv"))

df.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
s=df["population"]/100, label="population", figsize=(10,7),
c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,)

plt.legend()
plt.show()