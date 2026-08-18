def MarvellousLinearRegression():
    print("-" * 50)
    print("Simple Linear Regression - Manual")
    print("-" * 50)

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    # Calculate Mean of X and Y
    mean_x = sum(X) / len(X)
    mean_y = sum(Y) / len(Y)

    print("Mean of X =", mean_x)
    print("Mean of Y =", mean_y)
    

    # Calculate Slope
    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator
    print("-" * 50)

    # Calculate Intercept
    c = mean_y - (m * mean_x)

    print("Slope (m) =", m)
    print("Intercept (c) =", c)
    print("-" * 50)

    # Regression Equation
    print("Regression Equation:")
    print("Y =", m, "X +", c)
    print("-" * 50)

    # Predict Y for X = 6
    x = 6
    y = (m * x) + c

    print("Predicted Y for X = 6 :", y)
    print("-" * 50)

def main():
    MarvellousLinearRegression()

if __name__ == "__main__":
    main()