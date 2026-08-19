import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def BreastCancer():

    # 1. Load and Explore the Dataset
    print("-" * 60)
    print("1. Load and Explore the Dataset")
    print("-" * 60)

    cancer = load_breast_cancer()

    X = cancer.data
    Y = cancer.target

    print("Dataset Shape :", X.shape)
    print("Number of Records :", X.shape[0])
    print("Number of Features :", X.shape[1])

    print("-" * 60)

    # 2. Data Preprocessing
    print("2. Data Preprocessing")
    print("-" * 60)

    df = pd.DataFrame(X, columns=cancer.feature_names)

    # Handle Missing Values
    print("Missing Values :", df.isnull().sum().sum())

    df = df.dropna()

    X = df.values

    print("Missing Values Handled")
    print("-" * 60)

    # 3. Exploratory Data Analysis
    print("3. Exploratory Data Analysis")
    print("-" * 60)

    # Summary Statistics
    print("Summary Statistics:")
    print(df.describe())

    print("-" * 60)

    # Feature Correlation Visualization
    plt.figure(figsize=(10, 8))

    plt.imshow(df.corr(), cmap="coolwarm", aspect="auto")
    plt.colorbar(label="Correlation")

    plt.xlabel("Features")
    plt.ylabel("Features")
    plt.title("Feature Correlation")

    plt.tight_layout()
    plt.show()

    print("Feature Correlation Visualization Done..")

    print("-" * 60)

    # 4. Split Dataset into Training and Testing Sets
    print("4. Training and Testing Data")
    print("-" * 60)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.3,
        random_state=42,
        stratify=Y
    )

    print("Training Dataset Size :", X_train.shape)
    print("Testing Dataset Size :", X_test.shape)

    print("-" * 60)

    # Feature Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Feature Scaling Completed")
    print("-" * 60)

    # 5. Build Machine Learning Classification Model
    print("5.  Build Classification Model")
    print("-" * 60)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("Predicted Values:")
    for i in range(len(Y_pred)):
        print(Y_pred[i], "->", cancer.target_names[Y_pred[i]])

    print("-" * 60)

    # 6. Model Evaluation
    print("6. Model Evaluation")
    print("-" * 60)

    # Accuracy
    print("Accuracy :", accuracy_score(Y_test, Y_pred))

    print("-" * 60)

    # Confusion Matrix
    print("Confusion Matrix:")
    print(confusion_matrix(Y_test, Y_pred))

    print("-" * 60)

    # Precision, Recall and F1-Score
    print("Classification Report:")
    print(classification_report(
        Y_test,
        Y_pred,
        target_names=cancer.target_names
    ))

    print("-" * 60)

def main():
    BreastCancer()

if __name__ == "__main__":
    main()