import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix


# Load Dataset
def LoadData():

    print("=" * 60)
    print("LOAD DATASET")
    print("=" * 60)

    df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

    print(df.head())

    print("-" * 60)

    return df


# Separate Input and Output Variables
def SeparateData(df):

    print("SEPARATE INPUT AND OUTPUT VARIABLES")
    print("=" * 60)

    X = df.drop("Fraud", axis=1)
    Y = df["Fraud"]

    print("Input Variables:")
    print(X.head())

    print("\nOutput Variable:")
    print(Y.head())

    print("-" * 60)

    return X, Y


# Split Dataset
def SplitData(X, Y):

    print("SPLIT DATASET")
    print("=" * 60)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.3,
        random_state=42
    )

    print("Training Data Shape :", X_train.shape)
    print("Testing Data Shape  :", X_test.shape)

    print("-" * 60)

    return X_train, X_test, Y_train, Y_test


# Evaluate Model
def EvaluateModel(Y_test, Y_pred):

    Accuracy = accuracy_score(Y_test, Y_pred)

    Precision = precision_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    Recall = recall_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    F1 = f1_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    Matrix = confusion_matrix(
        Y_test,
        Y_pred
    )

    print("Accuracy  :", Accuracy)
    print("Precision :", Precision)
    print("Recall    :", Recall)
    print("F1 Score  :", F1)

    print("\nConfusion Matrix:")
    print(Matrix)

    print("-" * 60)

    return Accuracy, Precision, Recall, F1


# 1. Decision Tree Classifier
def DecisionTreeModel(X_train, X_test, Y_train, Y_test):

    print("1. DECISION TREE CLASSIFIER")
    print("=" * 60)

    model = DecisionTreeClassifier(
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Result = EvaluateModel(
        Y_test,
        Y_pred
    )

    return Result


# 2. Bagging Classifier
def BaggingModel(X_train, X_test, Y_train, Y_test):

    print("2. BAGGING CLASSIFIER")
    print("=" * 60)

    model = BaggingClassifier(
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Result = EvaluateModel(
        Y_test,
        Y_pred
    )

    return Result


# 3. Random Forest Classifier
def RandomForestModel(X_train, X_test, Y_train, Y_test):

    print("3. RANDOM FOREST CLASSIFIER")
    print("=" * 60)

    model = RandomForestClassifier(
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Result = EvaluateModel(
        Y_test,
        Y_pred
    )

    return Result


# 4. AdaBoost Classifier
def AdaBoostModel(X_train, X_test, Y_train, Y_test):

    print("4. ADABOOST CLASSIFIER")
    print("=" * 60)

    model = AdaBoostClassifier(
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Result = EvaluateModel(
        Y_test,
        Y_pred
    )

    return Result


# 5. Voting Classifier
def VotingModel(X_train, X_test, Y_train, Y_test):

    print("5. VOTING CLASSIFIER")
    print("=" * 60)

    model = VotingClassifier(
        estimators=[
            ("DecisionTree",
             DecisionTreeClassifier(random_state=42)),

            ("Bagging",
             BaggingClassifier(random_state=42)),

            ("RandomForest",
             RandomForestClassifier(random_state=42)),

            ("AdaBoost",
             AdaBoostClassifier(random_state=42))
        ],
        voting="hard"
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Result = EvaluateModel(
        Y_test,
        Y_pred
    )

    return Result


# Final Comparison
def CompareResults(
        DecisionTree,
        Bagging,
        RandomForest,
        AdaBoost,
        Voting):

    print("FINAL COMPARISON")
    print("=" * 60)

    Result = pd.DataFrame({

        "Algorithm": [
            "Decision Tree",
            "Bagging",
            "Random Forest",
            "AdaBoost",
            "Voting"
        ],

        "Accuracy": [
            DecisionTree[0],
            Bagging[0],
            RandomForest[0],
            AdaBoost[0],
            Voting[0]
        ],

        "Precision": [
            DecisionTree[1],
            Bagging[1],
            RandomForest[1],
            AdaBoost[1],
            Voting[1]
        ],

        "Recall": [
            DecisionTree[2],
            Bagging[2],
            RandomForest[2],
            AdaBoost[2],
            Voting[2]
        ],

        "F1 Score": [
            DecisionTree[3],
            Bagging[3],
            RandomForest[3],
            AdaBoost[3],
            Voting[3]
        ]
    })

    print(Result)

    print("=" * 60)


def main():

    df = LoadData()

    X, Y = SeparateData(df)

    X_train, X_test, Y_train, Y_test = SplitData(
        X,
        Y
    )

    DecisionTree = DecisionTreeModel(
        X_train,
        X_test,
        Y_train,
        Y_test
    )

    Bagging = BaggingModel(
        X_train,
        X_test,
        Y_train,
        Y_test
    )

    RandomForest = RandomForestModel(
        X_train,
        X_test,
        Y_train,
        Y_test
    )

    AdaBoost = AdaBoostModel(
        X_train,
        X_test,
        Y_train,
        Y_test
    )

    Voting = VotingModel(
        X_train,
        X_test,
        Y_train,
        Y_test
    )

    CompareResults(
        DecisionTree,
        Bagging,
        RandomForest,
        AdaBoost,
        Voting
    )


if __name__ == "__main__":
    main()