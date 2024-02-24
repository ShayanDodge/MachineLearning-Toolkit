import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Get the index position of the column labeled 'B'
index_position_B = df.columns.get_loc('B')

print("Index position of 'B':", index_position_B)

