import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data
data = {'Color': ['Red', 'Green', 'Blue', 'Red', 'Blue']}
df = pd.DataFrame(data)

# Creating an instance of OneHotEncoder
onehot_encoder = OneHotEncoder()

# Transforming the categorical variable using one-hot encoding
onehot_encoded = onehot_encoder.fit_transform(df[['Color']])

# Converting the sparse matrix to a DataFrame for better visualization
onehot_df = pd.DataFrame(onehot_encoded.toarray(), columns=onehot_encoder.get_feature_names_out(['Color']))

# Displaying the original and one-hot encoded data
print("Original Data:")
print(df)
print("\nOne-Hot Encoded Data:")
print(onehot_df)
# Get the list of categories using the encoder’s categories_ instance variable
# print(onehot_encoder.categories_)