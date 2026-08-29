import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier




# 1. Load the Dataset
def LoadData():
    df = pd.read_csv("Customer_Loan_Approval.csv")
    print("1. LOAD THE DATASET")
    print(df.head())
    print("-" * 60)
    return df


# 2. Check for Missing Values
def CheckMissingValues(df):
    print("2. CHECK FOR MISSING VALUES")
    print(df.isnull().sum())
    print("-" * 60)


# 3. Separate Input and Output Variables
def SeparateInputOutput(df):
    print("3. SEPARATE INPUT AND OUTPUT VARIABLES")

    X = df.drop("LoanApproved", axis=1)
    Y = df["LoanApproved"]

    print("Input Variables:")
    print(X.head())

    print("\nOutput Variable:")
    print(Y.head())

    print("-" * 60)

    return X, Y


# 4. Split Dataset into Training and Testing Data
def SplitData(X, Y):
    print("4. SPLIT DATASET")

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.3, random_state=42
    )

    print("Training Data Shape :", X_train.shape)
    print("Testing Data Shape  :", X_test.shape)

    print("-" * 60)

    return X_train, X_test, Y_train, Y_test


# Feature Scaling
def ScaleData(X_train, X_test):
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled


# 5. Train Logistic Regression
def TrainLogisticRegression(X_train, X_test, Y_train):
    print("5. TRAIN LOGISTIC REGRESSION")

    model = LogisticRegression()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("Logistic Regression Training Completed")
    print("-" * 60)

    return model, Y_pred


# 6. Train Decision Tree
def TrainDecisionTree(X_train, X_test, Y_train):
    print("6. TRAIN DECISION TREE")

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("Decision Tree Training Completed")
    print("-" * 60)

    return model, Y_pred


# 7. Train KNN
def TrainKNN(X_train, X_test, Y_train):
    print("7. TRAIN KNN")

    model = KNeighborsClassifier()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("KNN Training Completed")
    print("-" * 60)

    return model, Y_pred


# 8. Calculate Individual Accuracy
def CalculateIndividualAccuracy(Y_test, Y_pred_logistic,Y_pred_tree, Y_pred_knn):

    print("8. CALCULATE INDIVIDUAL ACCURACY")

    LogisticAccuracy = accuracy_score(Y_test, Y_pred_logistic)
    TreeAccuracy = accuracy_score(Y_test, Y_pred_tree)
    KNNAccuracy = accuracy_score(Y_test, Y_pred_knn)

    print("Logistic Regression Accuracy :", LogisticAccuracy)
    print("Decision Tree Accuracy       :", TreeAccuracy)
    print("KNN Accuracy                 :", KNNAccuracy)

    print("-" * 60)

    return LogisticAccuracy, TreeAccuracy, KNNAccuracy


# 9. Create Hard Voting Classifier
def CreateHardVoting(X_train, X_test, Y_train):
    print("9. CREATE HARD VOTING CLASSIFIER")

    HardVoting = VotingClassifier(
        estimators=[
            ("lr", LogisticRegression()),
            ("dt", DecisionTreeClassifier(random_state=42)),
            ("knn", KNeighborsClassifier())
        ],
        voting="hard"
    )

    HardVoting.fit(X_train, Y_train)

    Y_pred = HardVoting.predict(X_test)

    print("Hard Voting Classifier Created")
    print("-" * 60)

    return Y_pred


# 10. Calculate Hard Voting Accuracy
def CalculateHardVotingAccuracy(Y_test, Y_pred):
    print("10. CALCULATE HARD VOTING ACCURACY")

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("Hard Voting Accuracy :", Accuracy)
    print("-" * 60)

    return Accuracy


# 11. Create Soft Voting Classifier
def CreateSoftVoting(X_train, X_test, Y_train):
    print("11. CREATE SOFT VOTING CLASSIFIER")

    SoftVoting = VotingClassifier(
        estimators=[
            ("lr", LogisticRegression()),
            ("dt", DecisionTreeClassifier(random_state=42)),
            ("knn", KNeighborsClassifier())
        ],
        voting="soft"
    )

    SoftVoting.fit(X_train, Y_train)

    Y_pred = SoftVoting.predict(X_test)

    print("Soft Voting Classifier Created")
    print("-" * 60)

    return Y_pred


# 12. Calculate Soft Voting Accuracy
def CalculateSoftVotingAccuracy(Y_test, Y_pred):
    print("12. CALCULATE SOFT VOTING ACCURACY")

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("Soft Voting Accuracy :", Accuracy)
    print("-" * 60)

    return Accuracy


# 13. Compare the Results
def CompareResults(LogisticAccuracy, TreeAccuracy, KNNAccuracy,HardVotingAccuracy, SoftVotingAccuracy):

    print("13. COMPARE THE RESULTS")

    Result = pd.DataFrame({
        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "KNN",
            "Hard Voting",
            "Soft Voting"
        ],
        "Accuracy": [
            LogisticAccuracy,
            TreeAccuracy,
            KNNAccuracy,
            HardVotingAccuracy,
            SoftVotingAccuracy
        ]
    })

    print(Result)
    print("-" * 60)


def main():

    df = LoadData()

    CheckMissingValues(df)

    X, Y = SeparateInputOutput(df)

    X_train, X_test, Y_train, Y_test = SplitData(X, Y)

    X_train_scaled, X_test_scaled = ScaleData(X_train, X_test)

    LogisticModel, Y_pred_logistic = TrainLogisticRegression(X_train_scaled, X_test_scaled, Y_train)

    DecisionTreeModel, Y_pred_tree = TrainDecisionTree(X_train, X_test, Y_train)

    KNNModel, Y_pred_knn = TrainKNN(X_train_scaled, X_test_scaled, Y_train)

    LogisticAccuracy, TreeAccuracy, KNNAccuracy = CalculateIndividualAccuracy(
        Y_test,
        Y_pred_logistic,
        Y_pred_tree,
        Y_pred_knn
    )

    Y_pred_hard = CreateHardVoting(X_train_scaled, X_test_scaled, Y_train)

    HardVotingAccuracy = CalculateHardVotingAccuracy(Y_test, Y_pred_hard)

    Y_pred_soft = CreateSoftVoting(X_train_scaled, X_test_scaled, Y_train)

    SoftVotingAccuracy = CalculateSoftVotingAccuracy(Y_test, Y_pred_soft)

    CompareResults(
        LogisticAccuracy,
        TreeAccuracy,
        KNNAccuracy,
        HardVotingAccuracy,
        SoftVotingAccuracy
    )


if __name__ == "__main__":
    main()