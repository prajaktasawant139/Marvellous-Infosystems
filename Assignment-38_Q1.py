import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# Load Dataset
# =========================================================

df = pd.read_csv("student_performance_ml.csv")

# =========================================================
# Question 1
# Load Dataset and Display Information
# =========================================================

print("\n==============================")
print("Question 1 : Dataset Information")
print("==============================")

print("\nFirst 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())

print("\nDataset Shape :", df.shape)

print("\nColumn Names")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nObservation :")
print("The dataset contains student academic information.")
print("It includes study hours, attendance, previous score,")
print("assignments completed, sleep hours, and final result.")

# =========================================================
# Question 2
# Count Total, Passed and Failed Students
# =========================================================

print("\n==============================")
print("Question 2 : Student Count")
print("==============================")

total_students = len(df)
passed = (df["FinalResult"] == 1).sum()
failed = (df["FinalResult"] == 0).sum()

print("Total Students :", total_students)
print("Passed Students :", passed)
print("Failed Students :", failed)

print("\nObservation :")
print("The dataset contains both passed and failed students.")
print("These values help understand the class distribution.")

# =========================================================
# Question 3
# Calculate Average, Maximum and Minimum Values
# =========================================================

print("\n==============================")
print("Question 3 : Statistical Analysis")
print("==============================")

print("Average Study Hours :", df["StudyHours"].mean())
print("Average Attendance :", df["Attendance"].mean())
print("Maximum Previous Score :", df["PreviousScore"].max())
print("Minimum Sleep Hours :", df["SleepHours"].min())

print("\nObservation :")
print("Average values summarize the overall student performance.")
print("Maximum and minimum values show the range of the dataset.")

# =========================================================
# Question 4
# Distribution of FinalResult
# =========================================================

print("\n==============================")
print("Question 4 : Final Result Distribution")
print("==============================")

distribution = df["FinalResult"].value_counts()

print(distribution)

percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("\nPercentage")
print(percentage)

print("\nObservation :")

if abs(percentage.iloc[0] - percentage.iloc[1]) < 10:
    print("The dataset is approximately balanced.")
else:
    print("The dataset is imbalanced because one class has more records.")

# =========================================================
# Question 5
# Analyze StudyHours and Attendance
# =========================================================

print("\n==============================")
print("Question 5 : StudyHours and Attendance Analysis")
print("==============================")

study = df.groupby("FinalResult")["StudyHours"].mean()
attendance = df.groupby("FinalResult")["Attendance"].mean()

print("\nAverage Study Hours by Final Result")
print(study)

print("\nAverage Attendance by Final Result")
print(attendance)

print("\nObservation :")

print("1. Students who study more generally have a higher chance of passing.")
print("2. Higher attendance is associated with better academic performance.")
print("3. Students with low attendance are more likely to fail.")
print("4. Study hours and attendance both positively affect the final result.")
print("5. These features are important for predicting student performance.")

# =========================================================
# Question 6
# Histogram of StudyHours
# =========================================================

print("\n==============================")
print("Question 6 : Histogram of StudyHours")
print("==============================")

plt.figure(figsize=(6,4))
plt.hist(df["StudyHours"], bins=5)
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()

print("Observation :")
print("The histogram shows how study hours are distributed.")
print("It helps identify the most common study-hour range among students.")

# =========================================================
# Question 7
# Scatter Plot of StudyHours vs PreviousScore
# =========================================================

print("\n==============================")
print("Question 7 : Scatter Plot")
print("==============================")

colors = df["FinalResult"].map({
    1: "green",
    0: "red"
})

plt.figure(figsize=(6,4))

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
print("Green points represent passed students.")
print("Red points represent failed students.")
print("Students with higher study hours and previous scores")
print("are more likely to pass.")

# =========================================================
# Question 8
# Box Plot of Attendance
# =========================================================

print("\n==============================")
print("Question 8 : Attendance Box Plot")
print("==============================")

plt.figure(figsize=(5,5))

plt.boxplot(df["Attendance"])

plt.title("Attendance Box Plot")
plt.ylabel("Attendance")
plt.show()

print("Observation :")
print("The box plot shows the spread of attendance values.")
print("Points outside the whiskers indicate possible outliers.")

# =========================================================
# Question 9
# AssignmentsCompleted vs FinalResult
# =========================================================

print("\n==============================")
print("Question 9 : Assignments Completed")
print("==============================")

plt.figure(figsize=(6,4))

plt.scatter(
    df["AssignmentsCompleted"],
    df["FinalResult"]
)

plt.title("Assignments Completed vs Final Result")
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.show()

print("Observation :")
print("Students completing more assignments")
print("generally have a higher probability of passing.")
print("Assignment completion positively influences performance.")

# =========================================================
# Question 10
# SleepHours vs FinalResult
# =========================================================

print("\n==============================")
print("Question 10 : SleepHours vs FinalResult")
print("==============================")

plt.figure(figsize=(6,4))

plt.scatter(
    df["SleepHours"],
    df["FinalResult"]
)

plt.title("SleepHours vs FinalResult")
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")
plt.show()

print("Observation :")
print("Adequate sleep is beneficial for health and learning.")
print("However, sleeping more alone does not guarantee success.")
print("Academic performance also depends on study hours,")
print("attendance, previous scores, and assignment completion.")

# =========================================================
# Program Completed
# =========================================================

print("\n==============================")
print("Program Completed Successfully")
print("==============================")