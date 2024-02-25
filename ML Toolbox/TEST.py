from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the California housing dataset
california_housing = fetch_california_housing()
X = california_housing.data
y = california_housing.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the RandomForestRegressor model
rf_model = RandomForestRegressor(n_estimators=100, max_depth=20, min_samples_split=2, min_samples_leaf=1, bootstrap=True)
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model on the test set
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error on Test Set:", mse)

# Analyze the errors
errors = y_test - y_pred

# Plot predicted vs. actual values
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs. Predicted Values")
plt.show()

# Plot the distribution of errors
plt.hist(errors, bins=20)
plt.xlabel("Errors")
plt.ylabel("Frequency")
plt.title("Distribution of Errors")
plt.show()

# Feature importances
feature_importances = rf_model.feature_importances_
feature_names = california_housing.feature_names

# Display or use the feature importances as needed
print("Feature Importances:", feature_importances)

# If you want to associate feature names with their importances
feature_importance_dict = dict(zip(feature_names, feature_importances))
print("Feature Importances (associated with feature names):", feature_importance_dict)