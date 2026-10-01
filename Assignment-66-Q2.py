import numpy as np
import matplotlib.pyplot as plt

# Accept input value
x = float(input("Enter a value between -10 and 10: "))

if x < -10 or x > 10:
    print("Please enter a value between -10 and 10.")
else:
    # Input values for plotting
    values = np.linspace(-10, 10, 100)

    # Activation functions
    sigmoid = 1 / (1 + np.exp(-values))
    relu = np.maximum(0, values)
    tanh = np.tanh(values)

    # Calculate activation values for entered input
    sigmoid_x = 1 / (1 + np.exp(-x))
    relu_x = max(0, x)
    tanh_x = np.tanh(x)

    print("Input Value :", x)
    print("Sigmoid :", sigmoid_x)
    print("ReLU :", relu_x)
    print("Tanh :", tanh_x)

    # Plot activation functions
    plt.plot(values, sigmoid, label="Sigmoid")
    plt.plot(values, relu, label="ReLU")
    plt.plot(values, tanh, label="Tanh")

    plt.xlabel("Input")
    plt.ylabel("Activation Output")
    plt.title("Activation Functions")
    plt.legend()
    plt.grid()
    plt.show()