import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data[:, (2, 3)] # petal length, petal width
y = iris.target

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.show()