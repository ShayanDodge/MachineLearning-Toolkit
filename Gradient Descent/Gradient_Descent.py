def update_w_and_b(data_x, data_y, w, b, alpha):
    dl_dw = 0.0
    dl_db = 0.0
    N = len(data_x)

    for i in range(N):
        dl_dw += -2*data_x[i]*(data_y[i] - (w*data_x[i] + b))
        dl_db += -2*(data_y[i] - (w*data_x[i] + b))

    # update w and b
    w = w - (1/float(N))*dl_dw*alpha
    b = b - (1/float(N))*dl_db*alpha

    return w, b

# The function that calculate the average loss function:
def loss_function(data_x, data_y, w, b):
    N = len(data_x)
    total_error = 0.0
    for i in range(N):
        total_error += (data_y[i] - (w*data_x[i] + b))**2
    return total_error / float(N)

# The function that loops over multiple epochs is shown below:
def train(data_x, data_y, w, b, alpha, epochs):
    for e in range(epochs):
        w, b = update_w_and_b(data_x, data_y, w, b, alpha)

        # log the progress
        if e % 400 == 0:
            print("epoch:", e, "loss: ", loss_function(data_x, data_y, w, b))

    return w, b

# The function that predict new result
def predict(x, w, b):
    return w * x + b