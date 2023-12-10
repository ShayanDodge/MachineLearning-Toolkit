### This code will estimate the relationship between TV advertising and sales 
## Call essential packages
import Gradient_Descent as gd
import numpy as np
import matplotlib.pyplot as plt

## Read data from csv file
data = np.loadtxt("Advertising.csv",delimiter=",", skiprows=1)
ads = data[:,1]
sale = data[:,4]

## New values
x_new = np.linspace(min(ads), max(ads), 100)

## Initialize display a result
x = np.array(ads)
y = np.array(sale)

## Call training functions 
for i in range(50):
    w = 0.0
    b = 0.0
    epochs = 0 + 20*i
    alpha = 0.0000001
    (w, b) = gd.train(ads, sale, w, b, alpha, epochs)

    ## predict the result of new x
    y_new = gd.predict(x_new, w, b)

    ## Display a result
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.plot(x_new, y_new)

    # Add labels and title
    plt.xlabel('TV advertisement')
    plt.ylabel('Sales')
    plt.title(f'epochs = {epochs}')

    # Show the plot
    plt.pause(1)