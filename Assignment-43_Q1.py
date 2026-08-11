import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def CheckAccuracy(X, Y, K):

    # Divide the dataset into two equal parts

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    # Create KNN model

    model = KNeighborsClassifier(n_neighbors=K)

    # Train the model

    model.fit(X_train, Y_train)

    # Predict testing data

    Y_pred = model.predict(X_test)

    # Calculate accuracy

    Accuracy = accuracy_score(Y_test, Y_pred)

    return Accuracy


def MarvellousClassifier(DataPath):

    border = "-" * 50

    # --------------------------------------------------
    # Step 1 : Get Data
    # --------------------------------------------------

    print(border)
    print("Step 1 : Get Data")
    print(border)

    # Load CSV file
    # index_col=0 is used because first column is serial number

    df = pd.read_csv(DataPath, index_col=0)

    print("Dataset Loaded Successfully")

    print(border)

    print("First 5 Records")
    print(df.head())

    print(border)

    print("Dataset Shape :", df.shape)

    print(border)

    # --------------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate Data
    # --------------------------------------------------

    print(border)
    print("Step 2 : Clean, Prepare and Manipulate Data")
    print(border)

    # Create LabelEncoder objects

    WeatherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    # Convert string values into numerical values

    df["Wether"] = WeatherEncoder.fit_transform(df["Wether"])

    df["Temperature"] = TemperatureEncoder.fit_transform(
        df["Temperature"]
    )

    df["Play"] = PlayEncoder.fit_transform(df["Play"])

    print("Data after Label Encoding")

    print(border)

    print(df.head())

    print(border)

    # Separate Input and Output

    X = df[["Wether", "Temperature"]]

    Y = df["Play"]

    print("Input Data :")

    print(X.head())

    print(border)

    print("Output Data :")

    print(Y.head())

    print(border)

    # --------------------------------------------------
    # Step 3 : Train Data
    # --------------------------------------------------

    print(border)
    print("Step 3 : Train Data")
    print(border)

    # Create KNN model with K = 3

    model = KNeighborsClassifier(n_neighbors=3)

    # Train model using complete dataset
    # As mentioned in the question

    model.fit(X, Y)

    print("KNN Model Trained Successfully")

    print(border)

    # --------------------------------------------------
    # Step 4 : Test Data
    # --------------------------------------------------

    print(border)
    print("Step 4 : Test Data")
    print(border)

    print("Available Weather Values :")

    print(WeatherEncoder.classes_)

    print(border)

    print("Available Temperature Values :")

    print(TemperatureEncoder.classes_)

    print(border)

    # Accept input from user

    Wether = input("Enter Wether : ")

    print(border)

    Temperature = input("Enter Temperature : ")

    print(border)

    # Check whether entered values are valid

    if Wether not in WeatherEncoder.classes_:

        print("Invalid Wether Value")

        return

    if Temperature not in TemperatureEncoder.classes_:

        print("Invalid Temperature Value")

        return

    # Convert input into numerical values

    WetherValue = WeatherEncoder.transform([Wether])[0]

    TemperatureValue = TemperatureEncoder.transform(
        [Temperature]
    )[0]

    # Create new data point

    NewData = pd.DataFrame(
        [[WetherValue, TemperatureValue]],
        columns=["Wether", "Temperature"]
    )

    # Predict result

    Prediction = model.predict(NewData)

    Result = PlayEncoder.inverse_transform(Prediction)

    print("Predicted Result :", Result[0])

    print(border)

    # --------------------------------------------------
    # Step 5 : Calculate Accuracy
    # --------------------------------------------------

    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    K_values = [1, 3, 5]

    AccuracyValues = []

    for K in K_values:

        Accuracy = CheckAccuracy(X, Y, K)

        AccuracyValues.append(Accuracy)

        print(
            "K =",
            K,
            "Accuracy =",
            Accuracy * 100,
            "%"
        )

    print(border)

    print("Accuracy Calculation Completed")

    print(border)

    # --------------------------------------------------
    # Graphical Representation
    # --------------------------------------------------

    print(border)
    print("Graphical Representation")
    print(border)

    plt.figure(figsize=(8, 5))

    plt.plot(
        K_values,
        AccuracyValues,
        marker="o"
    )

    plt.title("K Values vs Accuracy")

    plt.xlabel("Value of K")

    plt.ylabel("Accuracy")

    plt.xticks(K_values)

    plt.grid(True)

    plt.show()

    print("Graphical Representation Completed")

    print(border)


def main():

    MarvellousClassifier(
        "MarvellousInfosystems_PlayPredictor.csv"
    )


if __name__ == "__main__":
    main()