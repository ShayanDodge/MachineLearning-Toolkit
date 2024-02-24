from sklearn import datasets
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LinearRegression

# Load the Iris dataset (Note: Linear Regression is not ideal for classification)
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Create a Linear Regression model
linear_model = LinearRegression()

# Create a KFold object with 5 folds
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Use cross_val_score to perform K-fold cross-validation and obtain R-squared scores
r2_scores = cross_val_score(linear_model, X, y, cv=kf, scoring='r2')

# Print the cross-validation scores
print("Cross-validation R-squared scores:", r2_scores)

# Calculate and print the mean and standard deviation of the R-squared scores
print("Mean R-squared: {:.2f}".format(r2_scores.mean()))
print("Standard deviation: {:.2f}".format(r2_scores.std()))