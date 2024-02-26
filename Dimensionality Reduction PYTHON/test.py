import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_swiss_roll

# Generate Swiss roll dataset
n_samples = 1000
noise = 0.5
X, color = make_swiss_roll(n_samples=n_samples, noise=noise)

# Plot the Swiss roll
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)

ax.set_title("Swiss Roll Dataset")
plt.show()
