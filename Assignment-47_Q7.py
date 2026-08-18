import pandas as pd
from sklearn.linear_model import LinearRegression


def MarvellousLinearRegression():

    border = "-" * 50

    print(border)
    print("Marvellous Linear Regression")
    print(border)

    # Dataset
    Data = {
        'StudyHours': [1, 2, 3, 4, 5],
        'Marks': [50, 55, 60, 65, 70]
    }

    df = pd.DataFrame(Data)

    print("Dataset : ")
    print(df)

    print(border)

    # Independent Variable
    X = df[['StudyHours']]

    # Dependent Variable
    Y = df['Marks']

    # Create Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X, Y)

    print("Regression Model Trained Successfully")

    print(border)

    # Print coefficient
    print("Coefficient : ", model.coef_[0])

    # Print intercept
    print("Intercept : ", model.intercept_)

    print(border)


def main():
    MarvellousLinearRegression()


if __name__ == "__main__":
    main()