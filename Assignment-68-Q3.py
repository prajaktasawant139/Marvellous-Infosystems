import numpy as np


# Flattens a 2D matrix into a 1D vector
def flatten(matrix):
    return matrix.flatten()


# Simulates a Fully Connected (Dense) Layer: output = dot(x, weights) + bias
def fully_connected_layer(vector, weights, bias):
    return np.dot(vector, weights) + bias


# Task 1: Take a 2D matrix
matrix = np.array([[6, 4], [8, 6]])

print("--- Task 1: Input Matrix ---")
print(matrix)
print()

# Task 2: Convert it into a 1D vector (Flattening)
flattened_vector = flatten(matrix)

print("--- Task 2: Flatten Output ---")
print(flattened_vector)
print()

# Task 3: Pass it to a fully connected layer
# Defining weights (4 inputs -> 2 output neurons) and biases
weights = np.array(
    [[0.5, 0.2], [0.1, 0.4], [0.3, 0.1], [0.2, 0.5]]  # Weight for neuron 1 & 2
)
bias = np.array([1.0, 0.5])

fc_output = fully_connected_layer(flattened_vector, weights, bias)

print("--- Task 3: Fully Connected Layer Output ---")
print(fc_output)
print()

# Task 4: Calculate final output manually to verify
# Neuron 1 calculation: (6*0.5) + (4*0.1) + (8*0.3) + (6*0.2) + 1.0
n1 = (
    (flattened_vector[0] * weights[0, 0])
    + (flattened_vector[1] * weights[1, 0])
    + (flattened_vector[2] * weights[2, 0])
    + (flattened_vector[3] * weights[3, 0])
    + bias[0]
)

# Neuron 2 calculation: (6*0.2) + (4*0.4) + (8*0.1) + (6*0.5) + 0.5
n2 = (
    (flattened_vector[0] * weights[0, 1])
    + (flattened_vector[1] * weights[1, 1])
    + (flattened_vector[2] * weights[2, 1])
    + (flattened_vector[3] * weights[3, 1])
    + bias[1]
)

manual_output = np.array([n1, n2])

print("--- Task 4: Manual Calculation Verification ---")
print(f"Neuron 1: 6*0.5 + 4*0.1 + 8*0.3 + 6*0.2 + 1.0 = {n1}")
print(f"Neuron 2: 6*0.2 + 4*0.4 + 8*0.1 + 6*0.5 + 0.5 = {n2}")
print(f"Manual Output Array: {manual_output}")
print()

# Task 5: Explanation of the role of the Flatten layer in CNN
print("--- Task 5: Role of Flatten Layer in CNN ---")
print(
    """
1. Bridge Between Convolutional & Dense Layers:
   Convolutional and Pooling layers output 2D/3D feature maps (spatial data).
   Fully Connected (Dense) layers require 1D vector inputs. The Flatten layer 
   bridges this gap by reshaping multi-dimensional matrices into a 1D array.

2. Preserving Features for Classification:
   Flattening unrolls all extracted spatial features into a continuous sequential array
   without losing or altering any learned numerical data, making it ready for final 
   classification decisions.
"""
)