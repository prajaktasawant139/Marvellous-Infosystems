# Take input, weight, bias, target output and learning rate
x = 2
weight = 0.5
bias = 0.1
target = 2.0
learning_rate = 0.1

# Calculate prediction
prediction = (x * weight) + bias

# Calculate error
error = target - prediction

# Store old weight
old_weight = weight

# Update weight using gradient descent logic
weight = weight + (learning_rate * error * x)

# Display results
print("Input :", x)
print("Old Weight :", old_weight)
print("Bias :", bias)
print("Target Output :", target)
print("Prediction :", prediction)
print("Error :", error)
print("Updated Weight :", weight)