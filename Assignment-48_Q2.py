def main():
    print("-" * 50)
    print("Simple Linear Regression Model Performance")
    print("-" * 50)

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    mean_x = sum(X) / len(X)
    mean_y = sum(Y) / len(Y)

    # Calculate slope
    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    # Calculate intercept
    c = mean_y - (m * mean_x)

    print("Regression Equation:")
    print("Y =", m, "X +", c)

    print("-" * 50)
    print("Predicted Y Values")
    print("-" * 50)

    predicted_y = []

    for x in X:
        y = (m * x) + c
        predicted_y.append(y)
        print("X =", x, "Actual Y =", Y[x - 1],
              "Predicted Y =", y)

    print("-" * 50)
    print("MSE Calculation")
    print("-" * 50)

    squared_error_sum = 0

    for i in range(len(Y)):
        error = Y[i] - predicted_y[i]
        squared_error = error ** 2

        print("Actual =", Y[i],
              "Predicted =", predicted_y[i],
              "Error =", error,
              "Squared Error =", squared_error)

        squared_error_sum = squared_error_sum + squared_error

    mse = squared_error_sum / len(Y)

    print("Sum of Squared Errors =", squared_error_sum)
    print("Mean Squared Error =", mse)

    # Calculate R2 Score
    total_sum = 0

    for y in Y:
        total_sum = total_sum + ((y - mean_y) ** 2)

    r2 = 1 - (squared_error_sum / total_sum)

    print("-" * 50)
    print("R2 Score =", r2)
    print("-" * 50)


if __name__ == "__main__":
    main()