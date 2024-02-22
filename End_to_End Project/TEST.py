import pandas as pd

# Sample data
data = {
    'column1': [1, 2, 3],
    'column2': ['A', 'B', 'C'],
    'column3': [10.1, 20.2, 30.3]}

# Create a DataFrame
df = pd.DataFrame(data)

# Extract column names
column_names = df.columns.tolist()

# Print the column names
print("Column Names:", column_names)
