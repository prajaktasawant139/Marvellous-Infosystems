import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------
df = pd.read_csv("student_performance_ml.csv")

print("First 5 Records")
print(df.head())

print("\nDataset Shape :", df.shape)

# ---------------------------------------------------------
# Features and Target
# ---------------------------------------------------------
X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.30, random_state=42
)

# ---------------------------------------------------------
# Train Decision Tree Model
# ---------------------------------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

train_acc = accuracy_score(Y_train, model.predict(X_train)) * 100
test_acc = accuracy_score(Y_test, Y_pred) * 100

print("\n==============================")
print("Original Model")
print("==============================")
print("Training Accuracy :", train_acc)
print("Testing Accuracy  :", test_acc)

# =========================================================
# Question 1
# Feature Importance
# =========================================================
print("\n==============================")
print("Question 1 : Feature Importance")
print("==============================")

importance = pd.Series(model.feature_importances_, index=X.columns)

print(importance)

print("\nMost Important Feature :", importance.idxmax())
print("Least Important Feature :", importance.idxmin())

# =========================================================
# Confusion Matrix
# =========================================================
print("\nConfusion Matrix")

cm = confusion_matrix(Y_test, Y_pred)
print(cm)

ConfusionMatrixDisplay(confusion_matrix=cm).plot()
plt.show()

# =========================================================
# Question 2
# Remove SleepHours
# =========================================================
print("\n==============================")
print("Question 2 : Remove SleepHours")
print("==============================")

X2 = df.drop(["FinalResult", "SleepHours"], axis=1)

Xt, Xs, Yt, Ys = train_test_split(
    X2,
    Y,
    test_size=0.30,
    random_state=42
)

m2 = DecisionTreeClassifier(random_state=42)
m2.fit(Xt, Yt)

acc_without_sleep = accuracy_score(Ys, m2.predict(Xs)) * 100

print("Original Accuracy :", test_acc)
print("Accuracy without SleepHours :", acc_without_sleep)

if acc_without_sleep > test_acc:
    print("Observation : Accuracy Improved.")
elif acc_without_sleep < test_acc:
    print("Observation : Accuracy Decreased.")
else:
    print("Observation : Accuracy Remained Same.")

# =========================================================
# Question 3
# Only StudyHours and Attendance
# =========================================================
print("\n==============================")
print("Question 3 : Two Feature Model")
print("==============================")

X3 = df[["StudyHours", "Attendance"]]

Xt, Xs, Yt, Ys = train_test_split(
    X3,
    Y,
    test_size=0.30,
    random_state=42
)

m3 = DecisionTreeClassifier(random_state=42)
m3.fit(Xt, Yt)

two_feature_acc = accuracy_score(Ys, m3.predict(Xs)) * 100

print("Accuracy using StudyHours and Attendance :", two_feature_acc)

if test_acc > two_feature_acc:
    print("Best Model : Original model performs better.")
elif test_acc < two_feature_acc:
    print("Best Model : Two-feature model performs better.")
else:
    print("Both models give same accuracy.")

# =========================================================
# Question 4
# Predict New Students
# =========================================================
print("\n==============================")
print("Question 4 : Predict New Students")
print("==============================")

new_students = pd.DataFrame({
    "StudyHours":[2,4,6,8,5],
    "Attendance":[60,75,85,95,80],
    "PreviousScore":[45,55,66,90,70],
    "AssignmentsCompleted":[3,5,7,9,6],
    "SleepHours":[5,6,7,8,7]
})

new_students["Prediction"] = model.predict(new_students)

new_students["Prediction"] = new_students["Prediction"].map({
    0:"Fail",
    1:"Pass"
})

print(new_students)

# =========================================================
# Question 5
# Manual Accuracy
# =========================================================
print("\n==============================")
print("Question 5 : Manual Accuracy")
print("==============================")

correct = (Y_test.values == Y_pred).sum()
manual_accuracy = (correct / len(Y_test)) * 100

print("Correct Predictions :", correct)
print("Total Records :", len(Y_test))
print("Manual Accuracy :", manual_accuracy)

# =========================================================
# Question 6
# Misclassified Students
# =========================================================
print("\n==============================")
print("Question 6 : Misclassified Students")
print("==============================")

misclassified = X_test[Y_test != Y_pred]

print(misclassified)

print("\nNumber of Misclassified Students :", len(misclassified))

print("\nObservation :")
print("These students were predicted incorrectly by the model.")
print("Possible reasons are overlapping feature values or insufficient training data.")

# =========================================================
# Question 7
# Compare Random States
# =========================================================
print("\n==============================")
print("Question 7 : Compare Random States")
print("==============================")

for state in [0, 10, 42]:

    Xt, Xs, Yt, Ys = train_test_split(
        X,
        Y,
        test_size=0.30,
        random_state=state
    )

    dt = DecisionTreeClassifier(random_state=state)

    dt.fit(Xt, Yt)

    acc = accuracy_score(Ys, dt.predict(Xs)) * 100

    print("Random State =", state, " Accuracy =", acc)

print("\nObservation :")
print("Changing random_state changes the train-test split.")
print("Hence accuracy may change slightly.")

# =========================================================
# Question 8
# Decision Tree Visualization
# =========================================================
print("\n==============================")
print("Question 8 : Decision Tree")
print("==============================")

plt.figure(figsize=(14,8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Fail","Pass"],
    filled=True
)

plt.show()

root_feature = X.columns[model.tree_.feature[0]]

print("Root Node Feature :", root_feature)

print("Reason :")
print("The root node is selected because it provides the highest Information Gain (best split).")

# =========================================================
# Question 9
# Performance Index
# =========================================================
print("\n==============================")
print("Question 9 : Performance Index")
print("==============================")

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X4 = df.drop("FinalResult", axis=1)

Xt, Xs, Yt, Ys = train_test_split(
    X4,
    Y,
    test_size=0.30,
    random_state=42
)

m4 = DecisionTreeClassifier(random_state=42)

m4.fit(Xt, Yt)

performance_acc = accuracy_score(
    Ys,
    m4.predict(Xs)
) * 100

print("Accuracy Before :", test_acc)
print("Accuracy After Adding PerformanceIndex :", performance_acc)

if performance_acc > test_acc:
    print("Observation : Accuracy Improved.")
elif performance_acc < test_acc:
    print("Observation : Accuracy Decreased.")
else:
    print("Observation : No Change in Accuracy.")

# =========================================================
# Question 10
# max_depth=None
# =========================================================
print("\n==============================")
print("Question 10 : max_depth=None")
print("==============================")

m5 = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

m5.fit(X_train, Y_train)

train = accuracy_score(
    Y_train,
    m5.predict(X_train)
) * 100

test = accuracy_score(
    Y_test,
    m5.predict(X_test)
) * 100

print("Training Accuracy :", train)
print("Testing Accuracy :", test)

print("\nObservation :")

if train == 100 and test < train:
    print("Training accuracy is 100% while testing accuracy is lower.")
    print("This indicates Overfitting.")
    print("The model memorizes the training data and performs less effectively on unseen data.")
else:
    print("The model generalizes reasonably well.")

print("\n==============================")
print("Program Completed Successfully")
print("==============================")