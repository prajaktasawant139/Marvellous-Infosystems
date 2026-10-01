import math

# Actual and predicted values
actual = [1, 0, 1, 1, 0]
predicted = [0.9, 0.2, 0.8, 0.7, 0.1]

# Mean Squared Error
mse = 0

for i in range(len(actual)):
    error = actual[i] - predicted[i]
    mse = mse + error ** 2

mse = mse / len(actual)

# Binary Cross Entropy
bce = 0

for i in range(len(actual)):
    p = min(max(predicted[i], 1e-15), 1 - 1e-15)

    loss = -(actual[i] * math.log(p) +
             (1 - actual[i]) * math.log(1 - p))

    bce = bce + loss

bce = bce / len(actual)

# Display losses
print("Actual Values    :", actual)
print("Predicted Values :", predicted)

print("Mean Squared Error :", mse)
print("Binary Cross Entropy :", bce)