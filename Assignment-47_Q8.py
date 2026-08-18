import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    print("-" * 50)
    print("Marvellous Linear Regression")
    print("-" * 50)

    # Dataset
    data = {
        "StudyHours": [1, 2, 3, 4, 5],
        "Marks": [50, 55, 60, 65, 70]
    }

    df = pd.DataFrame(data)

    print("Dataset :")
    print(df)

    print("-" * 50)

    # Independent variable
    X = df[["StudyHours"]]

    # Dependent variable
    Y = df["Marks"]

    # Create Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X, Y)

    print("Model trained successfully")
    print("-" * 50)

    # Display coefficient
    print("Coefficient : ", model.coef_[0])

    # Display intercept
    print("Intercept : ", model.intercept_)

    print("-" * 50)

    # Predict marks for 6 study hours
    StudyHours = pd.DataFrame([[6]], columns=["StudyHours"])

    prediction = model.predict(StudyHours)

    print("Study Hours :", 6)
    print("Predicted Marks : ", prediction[0])

    print("-" * 50)


if __name__ == "__main__":
    main()