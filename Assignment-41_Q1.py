import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# --------------------------------------------------
# Function Name : main
# Description   : Wine Classification using
#                 Decision Tree Classifier
# --------------------------------------------------

def main():

    # --------------------------------------------------
    # Step 1 : Get Data
    # --------------------------------------------------

    df = pd.read_csv("WinePredictor.csv")

    print("-----------------------------------------------")
    print("Wine Classification using Machine Learning")
    print("-----------------------------------------------")

    print("\nFirst 5 Records")
    print(df.head())

    print("\nDataset Shape :", df.shape)

    print("\nColumn Names")
    print(df.columns)

    print("\nTotal Records :", len(df))


    # --------------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate Data
    # --------------------------------------------------

    print("\nChecking Missing Values")
    print(df.isnull().sum())

    # Separate input features and target variable

    X = df.drop("Class", axis=1)

    Y = df["Class"]

    print("\nFeatures")
    print(X.columns)

    print("\nTarget :", Y.name)


    # --------------------------------------------------
    # Step 3 : Train Data
    # --------------------------------------------------

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.3,
        random_state=42
    )

    print("\nTraining Data :", X_train.shape)
    print("Testing Data  :", X_test.shape)

    # Create Decision Tree Model

    model = DecisionTreeClassifier(
        random_state=42
    )

    # Train Model

    model.fit(X_train, Y_train)

    print("\nModel Training Completed")


    # --------------------------------------------------
    # Step 4 : Test Data
    # --------------------------------------------------

    Y_pred = model.predict(X_test)

    print("\nActual Values")
    print(Y_test.values)

    print("\nPredicted Values")
    print(Y_pred)


    # --------------------------------------------------
    # Step 5 : Calculate Accuracy
    # --------------------------------------------------

    accuracy = accuracy_score(
        Y_test,
        Y_pred
    )

    print("\nAccuracy :", accuracy * 100, "%")


    # --------------------------------------------------
    # Final Result
    # --------------------------------------------------

    print("\n-----------------------------------------------")
    print("Wine Classification Completed Successfully")
    print("-----------------------------------------------")


# --------------------------------------------------
# Starter
# --------------------------------------------------

if __name__ == "__main__":
    main()