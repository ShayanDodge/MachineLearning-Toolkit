import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
import time

# Function to generate a unique run log directory based on the current timestamp
def get_run_logdir():
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join("logs", run_id)

# Create a simple dataset
X_train = np.random.rand(100, 8)
y_train = 3 * X_train[:, 0] + np.random.randn(100)

# Clear Keras session and set random seeds for reproducibility
keras.backend.clear_session()
np.random.seed(42)
tf.random.set_seed(42)

# Define a basic Keras Sequential model
model = keras.models.Sequential([
    keras.layers.Dense(30, activation="relu", input_shape=[8]),
    keras.layers.Dense(30, activation="relu"),
    keras.layers.Dense(1)
])

# Compile the model
model.compile(loss="mse", optimizer=keras.optimizers.SGD(learning_rate=1e-3))

# Create a TensorBoard callback
run_logdir = get_run_logdir()
tensorboard_cb = keras.callbacks.TensorBoard(run_logdir)

# Train the model with TensorBoard callback
history = model.fit(X_train, y_train, epochs=30, callbacks=[tensorboard_cb])