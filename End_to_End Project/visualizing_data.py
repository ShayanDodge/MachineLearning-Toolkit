import matplotlib.pyplot as ply
import numpy as np
import pandas as pd
import dataset_loader

# Loading the dataset
df = dataset_loader.load_data(dataset_loader.find_directory("datasets\housing\housing.csv"))

df.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
ply.show()