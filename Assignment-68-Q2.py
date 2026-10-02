import numpy as np


# Applies the ReLU (Rectified Linear Unit) activation function: f(x) = max(0, x)
def relu(x):
    return np.maximum(0, x)


# Applies 2x2 max pooling with default non-overlapping stride (stride=2)
def max_pooling_2x2(matrix, stride=2):
    h, w = matrix.shape
    pooled_h = (h - 2) // stride + 1
    pooled_w = (w - 2) // stride + 1

    output = np.zeros((pooled_h, pooled_w), dtype=matrix.dtype)

    for i in range(pooled_h):
        for j in range(pooled_w):
            window = matrix[
                i * stride : i * stride + 2, j * stride : j * stride + 2
            ]
            output[i, j] = np.max(window)

    return output


# Task 1: Create a feature map with positive and negative values
feature_map = np.array([[3, 3, 3], [0, 0, 0], [-3, -3, -3]])

print("--- Task 1: Input Feature Map ---")
print(feature_map)
print()

# Task 2: Apply ReLU
relu_output = relu(feature_map)

print("--- Task 2: Output after ReLU ---")
print(relu_output)
print()

# Task 3 & 4: Apply 2x2 Max Pooling and display output
pooled_output = max_pooling_2x2(relu_output)

print("--- Task 3 & 4: Output after 2x2 Max Pooling ---")
print(pooled_output)
print()

# Task 5: Print explanation of why pooling reduces size
print("--- Task 5: Why Pooling Reduces Size ---")
print(
    """
1. Downsampling via Windowing:
   Max pooling slides a filter window (e.g., 2x2) over spatial regions 
   of the feature map and retains only the single largest value per window, 
   discarding redundant neighboring pixels.

2. Mathematical Dimension Reduction:
   For an input size N x N, filter size F, and stride S, the output dimension is:
   Output Size = floor((N - F) / S) + 1

   Using a 2x2 filter with a stride of 2 halves both the height and width, 
   reducing the total number of elements by 75%.
"""
)