import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# =========================================================
# Student Performance Prediction using Decision Tree
# =========================================================

# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------

df = pd.read_csv("student_performance_ml.csv")

print("First 5 Records")
print(df.head())

print("\nDataset Shape :", df.shape)

# =========================================================
# Question 1
# Dataset Analysis
# =========================================================

print("\n==============================")
print("Question 1 : Dataset Analysis")
print("==============================")

passed = (df["FinalResult"] == 1).sum()
failed = (df["FinalResult"] == 0).sum()

print("Passed Students :", passed)
print("Failed Students :", failed)

print("\nAverage Study Hours :", df["StudyHours"].mean())
print("Average Attendance :", df["Attendance"].mean())

print("\nObservation :")
print("The dataset contains", passed, "passed students and", failed, "failed students.")
print("Average study hours and attendance help understand overall student performance.")

# =========================================================
# Question 2
# Data Visualization
# =========================================================

print("\n==============================")
print("Question 2 : Data Visualization")
print("==============================")

# Histogram

plt.figure(figsize=(7,5))

plt.hist(df["StudyHours"], bins=5)

plt.title("Study Hours Distribution")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.show()

print("Observation :")
print("Histogram shows how study hours are distributed among students.")

# Scatter Plot

colors = df["FinalResult"].map({
    1: "green",
    0: "red"
})

plt.figure(figsize=(7,5))

plt.scatter(
    df["StudyHours"],
    df["PreviousScore"],
    c=colors
)

plt.title("StudyHours vs PreviousScore")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.show()

print("Observation :")
print("Green points represent passed students while red points represent failed students.")

# Box Plot

plt.figure(figsize=(6,5))

plt.boxplot(df["Attendance"])

plt.title("Attendance Box Plot")

plt.show()

print("Observation :")
print("The box plot shows the spread of attendance values and possible outliers.")

# =========================================================
# Question 3
# Train-Test Split
# =========================================================

print("\n==============================")
print("Question 3 : Train-Test Split")
print("==============================")

X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.30,
    random_state=42
)

print("Training Records :", len(X_train))
print("Testing Records :", len(X_test))

print("\nObservation :")
print("70% of the dataset is used for training and 30% is used for testing.")

# =========================================================
# Question 4
# Train Decision Tree Model
# =========================================================

print("\n==============================")
print("Question 4 : Decision Tree Model Training")
print("==============================")

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

print("Model Trained Successfully.")

print("\nObservation :")
print("The Decision Tree model learns patterns from the training dataset.")

# =========================================================
# Question 5
# Prediction and Accuracy
# =========================================================

print("\n==============================")
print("Question 5 : Prediction and Accuracy")
print("==============================")

Y_pred = model.predict(X_test)

print("\nActual Values")
print(Y_test.values)

print("\nPredicted Values")
print(Y_pred)

test_accuracy = accuracy_score(Y_test, Y_pred) * 100
train_accuracy = accuracy_score(Y_train, model.predict(X_train)) * 100

print("\nTraining Accuracy :", train_accuracy)
print("Testing Accuracy :", test_accuracy)

print("\nObservation :")

if abs(train_accuracy - test_accuracy) < 5:
    print("Training and testing accuracies are close.")
    print("The model is well fitted.")
elif train_accuracy > test_accuracy:
    print("Training accuracy is much higher than testing accuracy.")
    print("The model may be overfitting.")
else:
    print("The model may be underfitting.")

# =========================================================
# Question 6
# Confusion Matrix
# =========================================================

print("\n==============================")
print("Question 6 : Confusion Matrix")
print("==============================")

cm = confusion_matrix(Y_test, Y_pred)

print(cm)

ConfusionMatrixDisplay(confusion_matrix=cm).plot()

plt.show()

print("\nObservation :")
print("True Positive (TP) : Correctly predicted Pass.")
print("True Negative (TN) : Correctly predicted Fail.")
print("False Positive (FP) : Predicted Pass but actually Fail.")
print("False Negative (FN) : Predicted Fail but actually Pass.")

# =========================================================
# Question 7
# Compare Different Tree Depths
# =========================================================

print("\n==============================")
print("Question 7 : Compare Different Tree Depths")
print("==============================")

for depth in [1, 3, None]:

    dt = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    dt.fit(X_train, Y_train)

    pred = dt.predict(X_test)

    acc = accuracy_score(Y_test, pred) * 100

    print("Max Depth =", depth, " Accuracy =", acc)

print("\nObservation :")
print("max_depth = 1 : Simple model, may underfit.")
print("max_depth = 3 : Balanced model.")
print("max_depth = None : Complete tree, may overfit.")

# =========================================================
# Question 8
# Predict New Student
# =========================================================

print("\n==============================")
print("Question 8 : Predict New Student")
print("==============================")

student = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "PreviousScore": [66],
    "AssignmentsCompleted": [7],
    "SleepHours": [7]
})

result = model.predict(student)

print("Student Details")
print(student)

if result[0] == 1:
    print("\nPrediction : Student will PASS")
else:
    print("\nPrediction : Student will FAIL")

print("\nObservation :")
print("The trained Decision Tree model predicts the result for the new student based on the given features.")

# =========================================================
# Final Conclusion
# =========================================================

print("\n==============================")
print("Final Conclusion")
print("==============================")

print("The Decision Tree model was successfully trained and tested.")
print("Different visualizations and evaluation metrics were used to analyze the model.")
print("The model can also predict the result of new students.")

print("\n==============================")
print("Program Completed Successfully")
print("==============================")