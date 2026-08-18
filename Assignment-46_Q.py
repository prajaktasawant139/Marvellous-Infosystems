import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def MarvellousLinearRegression(DataPath):

    border = "-" * 60

    # Step 1 : Get Data
    print(border)
    print("Step 1 : Get Data")
    print(border)

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully")
    print(border)

    print("Some entries from dataset : ")
    print(df.head())

    print(border)

    # Step 2 : Clean, Prepare and Manipulate Data
    print(border)
    print("Step 2 : Clean, Prepare and Manipulate Data")
    print(border)

    print("Shape of dataset : ", df.shape)
    print("Columns in dataset : ", df.columns.tolist())

    print(border)

    # Independent Variables
    X = df[['TV', 'radio', 'newspaper']]

    # Dependent Variable
    Y = df['sales']

    print("Independent Variables : ")
    print(X.head())

    print(border)

    print("Dependent Variable : ")
    print(Y.head())

    print(border)

    # Step 3 : Train Data
    print(border)
    print("Step 3 : Train Data")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    print("Training Data Details")
    print(border)

    print("Shape of X_train : ", X_train.shape)
    print("Shape of Y_train : ", Y_train.shape)

    print(border)

    print("Testing Data Details")
    print(border)

    print("Shape of X_test : ", X_test.shape)
    print("Shape of Y_test : ", Y_test.shape)

    print(border)

    # Create Linear Regression Model
    model = LinearRegression()

    print("Training Linear Regression Model...")
    print(border)

    # Train the model
    model.fit(X_train, Y_train)

    print("Model trained successfully")
    print(border)

    # Step 4 : Test the Data
    print(border)
    print("Step 4 : Test the Data")
    print(border)

    # Predict values
    Y_pred = model.predict(X_test)

    print("Testing completed successfully")
    print(border)

    # Step 5 : Display Predicted and Expected Values
    print(border)
    print("Step 5 : Display Predicted and Expected Values")
    print(border)

    print("Predicted Values        Expected Values")
    print(border)

    for predicted, expected in zip(Y_pred, Y_test):
        print(
            "Predicted : ",
            round(predicted, 2),
            "       Expected : ",
            expected
        )

    print(border)


def main():

    MarvellousLinearRegression("Advertising.csv")


if __name__ == "__main__":
    main()