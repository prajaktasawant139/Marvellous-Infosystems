import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def main():
    print("-" * 50)
    print("Marvellous Linear Regression")
    print("-" * 50)

    # Dataset
    data = {
        "Experience": [1, 2, 3, 4, 5],
        "Salary": [20000, 25000, 30000, 35000, 40000]
    }

    df = pd.DataFrame(data)

    print("Dataset :")
    print(df)

    print("-" * 50)

    # Independent variable
    X = df[["Experience"]]

    # Dependent variable
    Y = df["Salary"]

    # Create model
    model = LinearRegression()

    # Train model
    model.fit(X, Y)

    print("Model trained successfully")
    print("-" * 50)

    # Predict salary for 6 years
    experience = pd.DataFrame([[6]], columns=["Experience"])

    prediction = model.predict(experience)

    print("Predicted Salary for 6 Years Experience : ₹", prediction[0])

    print("-" * 50)

    # Plot data points
    plt.scatter(X, Y)

    # Plot regression line
    plt.plot(X, model.predict(X))

    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary - Linear Regression")

    plt.show()


if __name__ == "__main__":
    main()