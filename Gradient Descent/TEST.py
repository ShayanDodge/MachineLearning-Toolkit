import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'name': ['John', 'Alice', 'Bob'], 'age': [25, 30, 35]})

# Access the DataFrame
print(df)
# Access the first row of the DataFrame using iloc
# print(df.iloc[0,0])

# # Access the age of the second row of the DataFrame using loc
print(df[0])
