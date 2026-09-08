import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# 1. Load the Dataset
def LoadData():

    print("=" * 60)
    print("1. LOAD THE DATASET")
    print("=" * 60)

    df = pd.read_csv("Employee_Attrition.csv")

    print(df)

    print("-" * 60)

    return df


# 2. Display Shape, Columns and First Five Records
def DisplayData(df):

    print("2. DISPLAY SHAPE, COLUMNS AND FIRST FIVE RECORDS")
    print("=" * 60)

    print("Dataset Shape :", df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nFirst Five Records:")
    print(df.head())

    print("-" * 60)


# 3. Check for Missing Values
def CheckMissingValues(df):

    print("3. CHECK FOR MISSING VALUES")
    print("=" * 60)

    print(df.isnull().sum())

    print("-" * 60)


# 4. Identify Numerical and Categorical Features
def IdentifyFeatures(df):

    print("4. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES")
    print("=" * 60)

    NumericalFeatures = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    CategoricalFeatures = df.select_dtypes(
        include=["str"]
    ).columns

    print("Numerical Features:")
    print(list(NumericalFeatures))

    print("\nCategorical Features:")
    print(list(CategoricalFeatures))

    print("-" * 60)


# 5. Convert Categorical Feature into Numerical Representation
def ConvertCategorical(df):

    print("5. CONVERT CATEGORICAL FEATURE INTO NUMERICAL REPRESENTATION")
    print("=" * 60)

    df["OverTime"] = df["OverTime"].map({
        "No": 0,
        "Yes": 1
    })

    print(df["OverTime"].head())

    print("-" * 60)

    return df


# 6. Convert Target into 0 and 1
def ConvertTarget(df):

    print("6. CONVERT ATTRITION INTO 0 AND 1")
    print("=" * 60)

    df["Attrition"] = df["Attrition"].map({
        "No": 0,
        "Yes": 1
    })

    print(df["Attrition"].head())

    print("-" * 60)

    return df


# 7. Separate Independent and Dependent Variables
def SeparateVariables(df):

    print("7. SEPARATE INDEPENDENT AND DEPENDENT VARIABLES")
    print("=" * 60)

    X = df.drop("Attrition", axis=1)
    Y = df["Attrition"]

    print("Independent Variables:")
    print(X.head())

    print("\nDependent Variable:")
    print(Y.head())

    print("-" * 60)

    return X, Y


# 8. Divide Data into Training and Testing Data
def SplitData(X, Y):

    print("8. DIVIDE DATA INTO TRAINING AND TESTING DATA")
    print("=" * 60)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Data Shape :", X_train.shape)
    print("Testing Data Shape  :", X_test.shape)

    print("-" * 60)

    return X_train, X_test, Y_train, Y_test


# 9. Apply Feature Scaling
def ScaleData(X_train, X_test):

    print("9. APPLY FEATURE SCALING")
    print("=" * 60)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Feature Scaling Completed")

    print("-" * 60)

    return X_train_scaled, X_test_scaled, scaler


# 10. Design MLP Model
def CreateModel():

    print("10. DESIGN MLP MODEL")
    print("=" * 60)

    model = MLPClassifier(
        hidden_layer_sizes=(10, 5),
        max_iter=1000,
        random_state=42
    )

    print("MLP Model Created")
    print("Hidden Layers : 2")

    print("-" * 60)

    return model


# 11. Train the Network
def TrainModel(model, X_train, Y_train):

    print("11. TRAIN THE NETWORK")
    print("=" * 60)

    model.fit(X_train, Y_train)

    print("Training Completed")

    print("-" * 60)

    return model


# 12. Display Number of Iterations Required
def DisplayIterations(model):

    print("12. DISPLAY NUMBER OF ITERATIONS REQUIRED")
    print("=" * 60)

    print("Number of Iterations :", model.n_iter_)

    print("-" * 60)


# 13. Calculate Training Accuracy
def TrainingAccuracy(model, X_train, Y_train):

    print("13. CALCULATE TRAINING ACCURACY")
    print("=" * 60)

    Y_train_pred = model.predict(X_train)

    Accuracy = accuracy_score(
        Y_train,
        Y_train_pred
    )

    print("Training Accuracy :", Accuracy)

    print("-" * 60)


# 14. Calculate Testing Accuracy
def TestingAccuracy(model, X_test, Y_test):

    print("14. CALCULATE TESTING ACCURACY")
    print("=" * 60)

    Y_test_pred = model.predict(X_test)

    Accuracy = accuracy_score(
        Y_test,
        Y_test_pred
    )

    print("Testing Accuracy :", Accuracy)

    print("-" * 60)

    return Y_test_pred


# 15. Create Confusion Matrix
def ConfusionMatrix(Y_test, Y_test_pred):

    print("15. CREATE CONFUSION MATRIX")
    print("=" * 60)

    Matrix = confusion_matrix(
        Y_test,
        Y_test_pred
    )

    print(Matrix)

    print("-" * 60)


# 16. Plot Loss Curve
def PlotLossCurve(model):

    print("16. PLOT LOSS CURVE")
    print("=" * 60)

    plt.plot(model.loss_curve_)

    plt.title("MLP Loss Curve")
    plt.xlabel("Iterations")
    plt.ylabel("Loss")

    plt.show()

    print("-" * 60)


# 17. Function to Predict Employee Attrition
def PredictAttrition(model, scaler, employee):

    EmployeeData = pd.DataFrame(
        [employee],
        columns=[
            "Age",
            "MonthlyIncome",
            "YearsAtCompany",
            "TotalWorkingYears",
            "DistanceFromHome",
            "JobSatisfaction",
            "WorkLifeBalance",
            "OverTime",
            "NumCompaniesWorked",
            "TrainingTimesLastYear"
        ]
    )

    EmployeeData["OverTime"] = EmployeeData["OverTime"].map({
        "No": 0,
        "Yes": 1
    })

    EmployeeDataScaled = scaler.transform(
        EmployeeData
    )

    Prediction = model.predict(
        EmployeeDataScaled
    )

    return Prediction[0]


# 18. Test System Using Five New Employee Records
def TestNewEmployees(model, scaler):

    print("18. TEST SYSTEM USING FIVE NEW EMPLOYEE RECORDS")
    print("=" * 60)

    Employees = [

        [25, 30000, 2, 3, 10, 3, 3, "Yes", 2, 2],

        [45, 100000, 10, 18, 5, 4, 4, "No", 3, 4],

        [30, 50000, 4, 6, 20, 2, 2, "Yes", 4, 1],

        [28, 40000, 1, 4, 15, 2, 2, "Yes", 3, 2],

        [50, 120000, 12, 25, 5, 4, 4, "No", 2, 5]
    ]

    for i in range(len(Employees)):

        Prediction = PredictAttrition(
            model,
            scaler,
            Employees[i]
        )

        print(
            "Employee", i + 1,
            "Prediction :", Prediction
        )

        if Prediction == 0:
            print("Employee is likely to stay")
        else:
            print("Employee is likely to leave")

        print("-" * 60)


# 19. Explain Overfitting or Underfitting
def CheckModelFit(model, X_train, Y_train, X_test, Y_test):

    print("19. CHECK OVERFITTING OR UNDERFITTING")
    print("=" * 60)

    TrainingAccuracyValue = accuracy_score(
        Y_train,
        model.predict(X_train)
    )

    TestingAccuracyValue = accuracy_score(
        Y_test,
        model.predict(X_test)
    )

    print("Training Accuracy :", TrainingAccuracyValue)
    print("Testing Accuracy  :", TestingAccuracyValue)

    if TrainingAccuracyValue > TestingAccuracyValue:
        print("Observation: The model may be overfitting.")

    elif TrainingAccuracyValue < TestingAccuracyValue:
        print("Observation: The model may be underfitting.")

    else:
        print("Observation: The model is fitting the data properly.")

    print("-" * 60)


def main():

    # Step 1
    df = LoadData()

    # Step 2
    DisplayData(df)

    # Step 3
    CheckMissingValues(df)

    # Step 4
    IdentifyFeatures(df)

    # Step 5
    df = ConvertCategorical(df)

    # Step 6
    df = ConvertTarget(df)

    # Step 7
    X, Y = SeparateVariables(df)

    # Step 8
    X_train, X_test, Y_train, Y_test = SplitData(X, Y)

    # Step 9
    X_train_scaled, X_test_scaled, scaler = ScaleData(
        X_train,
        X_test
    )

    # Step 10
    model = CreateModel()

    # Step 11
    model = TrainModel(
        model,
        X_train_scaled,
        Y_train
    )

    # Step 12
    DisplayIterations(model)

    # Step 13
    TrainingAccuracy(
        model,
        X_train_scaled,
        Y_train
    )

    # Step 14
    Y_test_pred = TestingAccuracy(
        model,
        X_test_scaled,
        Y_test
    )

    # Step 15
    ConfusionMatrix(
        Y_test,
        Y_test_pred
    )

    # Step 16
    PlotLossCurve(model)

    # Step 18
    TestNewEmployees(
        model,
        scaler
    )

    # Step 19
    CheckModelFit(
        model,
        X_train_scaled,
        Y_train,
        X_test_scaled,
        Y_test
    )


if __name__ == "__main__":
    main()