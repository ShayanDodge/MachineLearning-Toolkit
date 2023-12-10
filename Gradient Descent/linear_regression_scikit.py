### This code will estimate the relationship between TV advertising and sales 
## Call essential packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

## Read data from csv file
data = np.loadtxt("Advertising.csv",delimiter=",", skiprows=1)
ads = data[:,1]
X = np.reshape(ads,(-1,1))
sale = data[:,-1]

## New values
x_new = np.linspace(min(ads), max(ads), 100)
x_new = np.reshape(x_new,(-1,1))
## Initialize display a result
x = np.array(ads)
y = np.array(sale)

## Call training functions 
model = LinearRegression().fit(X, sale)

## predict the result of new x
y_new = model.predict(x_new)
## Display a result
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.plot(x_new, y_new)

# Add labels and title
plt.xlabel('TV advertisement')
plt.ylabel('Sales')
plt.title("scikit-learn")

# Show the plot
plt.show()
plt.pause(1)