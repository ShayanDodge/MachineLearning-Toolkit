import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Create a DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}

df = pd.DataFrame(data)

# Create a scatter matrix
scatter_matrix(df, alpha=0.8, figsize=(8, 8), diagonal='hist')

# Show the plot
plt.show()