import pandas as pd
import matplotlib.pyplot as plt
import warnings

from sklearn.exceptions import ConvergenceWarning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


warnings.filterwarnings("ignore", category=ConvergenceWarning)


def LoadDataset():
    print("=" * 60)
    print("1. LOAD AND UNDERSTAND THE DATASET")
    print("=" * 60)

    df = pd.read_csv("Loan_Default.csv")

    print(df)
    print("\nDataset Shape :", df.shape)
    print("\nColumns :", df.columns.tolist())

    return df


def ExploratoryAnalysis(df):
    print("\n" + "=" * 60)
    print("2. PERFORM EXPLORATORY ANALYSIS")
    print("=" * 60)

    print("\nFirst 5 Records :")
    print(df.head())

    print("\nDataset Information :")
    df.info()

    print("\nStatistical Summary :")
    print(df.describe())


def FindMissingValues(df):
    print("\n" + "=" * 60)
    print("3. FIND MISSING VALUES")
    print("=" * 60)

    print(df.isnull().sum())


def CheckClassBalance(df):
    print("\n" + "=" * 60)
    print("4. CHECK WHETHER THE TARGET CLASSES ARE BALANCED")
    print("=" * 60)

    print(df["Default"].value_counts())


def EncodeCategoricalVariables(df):
    print("\n" + "=" * 60)
    print("5. ENCODE CATEGORICAL VARIABLES")
    print("=" * 60)

    df["PreviousDefault"] = df["PreviousDefault"].map({
        "No": 0,
        "Yes": 1
    })

    df["HomeOwnership"] = df["HomeOwnership"].map({
        "Rent": 0,
        "Own": 1,
        "Mortgage": 2
    })

    print(df.head())

    return df


def SeparateXY(df):
    print("\n" + "=" * 60)
    print("6. SEPARATE X AND Y")
    print("=" * 60)

    X = df.drop("Default", axis=1)
    Y = df["Default"]

    print("Independent Variables (X) :")
    print(X)

    print("\nDependent Variable (Y) :")
    print(Y)

    return X, Y


def SplitData(X, Y):
    print("\n" + "=" * 60)
    print("7. SPLIT DATASET INTO TRAINING AND TESTING DATA")
    print("=" * 60)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("X_train Shape :", X_train.shape)
    print("X_test Shape  :", X_test.shape)
    print("Y_train Shape :", Y_train.shape)
    print("Y_test Shape  :", Y_test.shape)

    return X_train, X_test, Y_train, Y_test


def ExplainStratifiedSplitting():
    print("\n" + "=" * 60)
    print("8. STRATIFIED SPLITTING")
    print("=" * 60)

    print("Yes, stratified splitting should be used because")
    print("the target classes are imbalanced.")
    print("It maintains the same class proportion in training")
    print("and testing data.")


def ScaleFeatures(X_train, X_test):
    print("\n" + "=" * 60)
    print("9. SCALE THE FEATURES")
    print("=" * 60)

    Scaler = StandardScaler()

    X_train_scaled = Scaler.fit_transform(X_train)
    X_test_scaled = Scaler.transform(X_test)

    print("Feature scaling completed.")

    return X_train_scaled, X_test_scaled, Scaler


def CreateMLPClassifier():
    print("\n" + "=" * 60)
    print("10. CREATE AN MLP CLASSIFIER")
    print("=" * 60)

    Model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    print(Model)

    return Model


def TrainModel(Model, X_train_scaled, Y_train):
    print("\n" + "=" * 60)
    print("11. TRAIN THE MODEL")
    print("=" * 60)

    Model.fit(X_train_scaled, Y_train)

    print("Model training completed.")

    return Model


def CalculateAccuracy(Model, X_train_scaled, X_test_scaled,
                      Y_train, Y_test):

    print("\n" + "=" * 60)
    print("12. CALCULATE ACCURACY")
    print("=" * 60)

    Y_train_pred = Model.predict(X_train_scaled)
    Y_test_pred = Model.predict(X_test_scaled)

    TrainAccuracy = accuracy_score(Y_train, Y_train_pred)
    TestAccuracy = accuracy_score(Y_test, Y_test_pred)

    print("Training Accuracy :", TrainAccuracy)
    print("Testing Accuracy  :", TestAccuracy)

    return Y_test_pred


def GenerateConfusionMatrix(Y_test, Y_test_pred):
    print("\n" + "=" * 60)
    print("13. GENERATE CONFUSION MATRIX")
    print("=" * 60)

    CM = confusion_matrix(Y_test, Y_test_pred)

    print(CM)


def CalculateMetrics(Y_test, Y_test_pred):
    print("\n" + "=" * 60)
    print("14. CALCULATE PRECISION, RECALL AND F1 SCORE")
    print("=" * 60)

    Precision = precision_score(Y_test, Y_test_pred)
    Recall = recall_score(Y_test, Y_test_pred)
    F1 = f1_score(Y_test, Y_test_pred)

    print("Precision :", Precision)
    print("Recall    :", Recall)
    print("F1 Score  :", F1)


def PlotLearningCurve(Model):
    print("\n" + "=" * 60)
    print("15. PLOT LEARNING CURVE")
    print("=" * 60)

    plt.plot(Model.loss_curve_)
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title("Learning Curve")
    plt.show()


def TestNewData(Model, Scaler, X):
    print("\n" + "=" * 60)
    print("16. TEST THE MODEL ON NEW DATA")
    print("=" * 60)

    NewData = pd.DataFrame([
        [30, 500000, 300000, 750, 5, 1, 20000, 24, 0, 1],
        [55, 250000, 800000, 580, 20, 4, 50000, 60, 1, 0],
        [28, 700000, 250000, 780, 3, 0, 15000, 36, 0, 1],
        [45, 400000, 600000, 620, 12, 2, 35000, 48, 1, 0],
        [35, 600000, 400000, 720, 8, 1, 25000, 36, 0, 2]
    ], columns=X.columns)

    NewDataScaled = Scaler.transform(NewData)

    Prediction = Model.predict(NewDataScaled)

    print("Predicted Default Values :")
    print(Prediction)


def HyperparameterExperiment(X_train_scaled, Y_train):
    print("\n" + "=" * 60)
    print("HYPERPARAMETER EXPERIMENT")
    print("=" * 60)

    print("Change one parameter at a time.")

    print("\nExperiment 1 - Activation")

    ActivationValues = [
        "identity",
        "logistic",
        "tanh",
        "relu"
    ]

    for Activation in ActivationValues:

        Model = MLPClassifier(
            hidden_layer_sizes=(32, 16),
            activation=Activation,
            solver="adam",
            max_iter=1000,
            random_state=42
        )

        Model.fit(X_train_scaled, Y_train)

        print(Activation, ":", Model.n_iter_)

    print("\nExperiment 2 - Hidden Layers")

    HiddenLayerValues = [
        (10,),
        (20, 10),
        (50,25),
        (100, 50, 25)
    ]

    for HiddenLayers in HiddenLayerValues:

        Model = MLPClassifier(
            hidden_layer_sizes=HiddenLayers,
            activation="relu",
            solver="adam",
            max_iter=1000,
            random_state=42
        )

        Model.fit(X_train_scaled, Y_train)

        print(HiddenLayers, ":", Model.n_iter_)

    print("\nExperiment 3 - Learning Rate")

    LearningRateValues = [
        0.001,
        0.01,
        0.1
    ]

    for LearningRate in LearningRateValues:

        Model = MLPClassifier(
            hidden_layer_sizes=(32, 16),
            activation="relu",
            solver="adam",
            learning_rate_init=LearningRate,
            max_iter=1000,
            random_state=42
        )

        Model.fit(X_train_scaled, Y_train)

        print(LearningRate, ":", Model.n_iter_)


def main():

    df = LoadDataset()

    ExploratoryAnalysis(df)

    FindMissingValues(df)

    CheckClassBalance(df)

    df = EncodeCategoricalVariables(df)

    X, Y = SeparateXY(df)

    X_train, X_test, Y_train, Y_test = SplitData(X, Y)

    ExplainStratifiedSplitting()

    X_train_scaled, X_test_scaled, Scaler = ScaleFeatures(
        X_train,
        X_test
    )

    Model = CreateMLPClassifier()

    Model = TrainModel(
        Model,
        X_train_scaled,
        Y_train
    )

    Y_test_pred = CalculateAccuracy(
        Model,
        X_train_scaled,
        X_test_scaled,
        Y_train,
        Y_test
    )

    GenerateConfusionMatrix(
        Y_test,
        Y_test_pred
    )

    CalculateMetrics(
        Y_test,
        Y_test_pred
    )

    PlotLearningCurve(Model)

    TestNewData(
        Model,
        Scaler,
        X
    )

    HyperparameterExperiment(
        X_train_scaled,
        Y_train
    )


if __name__ == "__main__":
    main()