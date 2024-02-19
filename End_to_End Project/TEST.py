import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generating example data
np.random.seed(42)  # For reproducibility
num_points = 100
longitude = np.random.uniform(low=-180, high=180, size=num_points)
latitude = np.random.uniform(low=-90, high=90, size=num_points)

# Creating a DataFrame
df = pd.DataFrame({'longitude': longitude, 'latitude': latitude})

# Creating a scatter plot
df.plot(kind='scatter', x='longitude', y='latitude', title='Scatter Plot of Longitude vs Latitude')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()