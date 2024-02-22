import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from attribute_combination import CombinedAttributesAdder
import dataset_loader

#%% Simple example of pipeline
# # Sample data with missing values
# data = {
#     'feature1': [1, 2, None, 4, 5],
#     'feature2': [5, 6, 7, 8, 9],
#     'label': [0, 1, 0, 1, 0]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Split the data into features and labels
# X = df[['feature1', 'feature2']]
# y = df['label']

# # Define the pipeline
# pipeline = Pipeline(steps=[
#     ('imputer', SimpleImputer(strategy='mean')),  # Step 1: Impute missing values with the mean
#     ('scaler', StandardScaler())  # Step 2: Standardize the features
# ])

# # Fit the pipeline on the data
# X_transformed = pipeline.fit_transform(X)

# # Display the transformed data
# print("Transformed Data:\n", X_transformed)

#%% advance example of Piprline
# # Loading the dataset
# df = dataset_loader.load_data(dataset_loader.find_directory("datasets\housing\housing.csv"))

# # Removing non numeric data
# df = df.drop("ocean_proximity", axis=1)
# # print(df.head())

# num_pipeline = Pipeline([
# ('imputer', SimpleImputer(strategy="median")),
# ('attribs_adder', CombinedAttributesAdder()),
# ('std_scaler', StandardScaler()),
# ])

# data_num_tr = num_pipeline.fit_transform(df)
# df_tr = pd.DataFrame(data_num_tr)
# print(df_tr)

#%% simple example ColumnTransformer

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Sample data with both numerical and categorical columns
data = {
    'numeric_feature': [1, 2, None, 4, 5],
    'categorical_feature': ['A', 'B', 'A', 'B', 'A'],
    'label': [0, 1, 0, 1, 0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Split the data into features and labels
X = df[['numeric_feature', 'categorical_feature']]
y = df['label']

# Define the ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), ['numeric_feature']),
        ('cat', OneHotEncoder(), ['categorical_feature'])
    ])

# Create a simple pipeline with only the preprocessor
model = Pipeline(steps=[('preprocessor', preprocessor)])

# Fit the pipeline on the data
X_transformed = model.fit_transform(X)

# Display the transformed data
print("Transformed Data:\n", X_transformed)