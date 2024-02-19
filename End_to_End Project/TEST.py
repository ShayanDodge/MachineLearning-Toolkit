import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generating example data
np.random.seed(42)  # For reproducibility
num_points = 100
longitude = np.random.uniform(low=-180, high=180, size=num_points)
latitude = np.random.uniform(low=-90, high=90, size=num_points)
population = np.random.randint(100, 1000, size=num_points)
median_house_value = np.random.randint(50000, 200000, size=num_points)

# Creating a DataFrame
housing = pd.DataFrame({'longitude': longitude, 'latitude': latitude, 'population': population, 'median_house_value': median_house_value})

# Creating a scatter plot with various customizations
housing.plot(kind='scatter', x='longitude', y='latitude', alpha=0.4,
             s=housing["population"]/100, label="population", figsize=(10,7),
             c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True)
plt.legend()
plt.title('Scatter Plot with Population and Median House Value')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()