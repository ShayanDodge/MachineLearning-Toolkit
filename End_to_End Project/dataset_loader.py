import matplotlib.pyplot as plt
import pandas as pd
import sys
import os

# Function to find the directory of a file
def find_directory(filename=None):
    if filename is None:
        filename = sys.argv[1]
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, filename)
    return file_path

# Function to load the dataset from a CSV file
def load_data(csv_path):
    return pd.read_csv(csv_path)

# Load the dataset using the default path
if __name__ == "__main__":
    df = load_data(find_directory("datasets\housing\housing.csv"))
    print(df.head())
    print(df.info())
    df.hist(bins=50, figsize=(20,15))
    plt.show()