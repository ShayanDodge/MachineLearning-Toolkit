# This code will estimate the relationship between TV advertising and sales 
from csv import reader
import Gradient_Descent as gd
import numpy as np
import matplotlib.pyplot as plt

# Read data from csv file
infile  = open("Advertising.csv")
csvReader = reader (infile)
ads = []
sale = []
i = 0
for row in csvReader:
    if i > 0 :
        ads.append(float(row[1]))
        sale.append(float(row[4]))
    i += 1

# Call training functions 
for i in range(50):
    w = 0.0
    b = 0.0
    epochs = 0 + 20*i
    alpha = 0.0000001
    (w, b) = gd.train(ads, sale, w, b, alpha, epochs)

    # Test the result
    x_new = []
    y_new = []
    step = ((max(ads) - min(ads))/100)+1
    for j in range(100):
        x_new.append(min(ads) + j * step)
        y_new.append(gd.predict(min(ads) + j * step, w, b)) 

    # Display a result
    x = np.array(ads)
    y = np.array(sale)

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.plot(x_new, y_new)

    # Add labels and title
    plt.xlabel('TV advertisement')
    plt.ylabel('Sales')
    plt.title(f'epochs = {epochs}')

    # Show the plot
    plt.pause(1)
    
plt.show()


