from sklearn.preprocessing import MinMaxScaler
import numpy as np

# # Example data
# data = np.array([[1.0, 2.0],
#                  [3.0, 4.0],
#                  [5.0, 6.0]])

# # Instantiate MinMaxScaler with a custom feature_range
# scaler = MinMaxScaler(feature_range=(0, 1))

# # Fit and transform the data
# scaled_data = scaler.fit_transform(data)

# print("Original Data:\n", data)
# print("\nScaled Data:\n", scaled_data)

from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[1.0, 2.0],
                 [3.0, 4.0],
                 [5.0, 6.0]])

scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)
print("Original Data:\n", data)
print("\nScaled Data:\n", standardized_data)