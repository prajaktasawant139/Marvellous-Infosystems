import pandas as pd
from sklearn.linear_model import LinearRegression


def MarvellousMultipleLinearRegression():

    border = "-" * 50

    print(border)
    print("Marvellous Multiple Linear Regression")
    print(border)

    # Dataset
    Data = {
        'StudyHours': [1, 2, 3, 4, 5],
        'SleepHours': [7, 6, 7, 6, 8],
        'Marks': [50, 55, 60, 65, 70]
    }

    df = pd.DataFrame(Data)

    print("Dataset : ")
    print(df)

    print(border)

    # Independent Variables
    X = df[['StudyHours', 'SleepHours']]

    # Dependent Variable
    Y = df['Marks']

    # Create model
    model = LinearRegression()

    # Train model
    model.fit(X, Y)

    print("Regression Model Trained Successfully")

    print(border)

    # Print coefficients
    print("Coefficient of StudyHours : ", model.coef_[0])
    print("Coefficient of SleepHours : ", model.coef_[1])

    print(border)

    # Print intercept
    print("Intercept : ", model.intercept_)

    print(border)


def main():
    MarvellousMultipleLinearRegression()


if __name__ == "__main__":
    main()