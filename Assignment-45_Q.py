import pandas as pd
import matplotlib.pyplot as plt


def MarvellousDataFrame():
    border = "-" * 50

    # Original Dataset
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    # --------------------------------------------------
    # Q1. Normalize the 'Math' scores using Min-Max scaling
    # --------------------------------------------------

    print(border)
    print("Min-Max Scaling of Math Scores")
    print(border)

    df['Math_Normalized'] = (
        (df['Math'] - df['Math'].min()) /
        (df['Math'].max() - df['Math'].min())
    )

    print(df[['Name', 'Math', 'Math_Normalized']])

    # --------------------------------------------------
    # Q2. Create Gender column and perform One-Hot Encoding
    # --------------------------------------------------

    print("\n" + border)
    print("Gender Column and One-Hot Encoding")
    print(border)

    df['Gender'] = ['Male', 'Male', 'Female']

    print("DataFrame with Gender :")
    print(df)

    df = pd.get_dummies(df, columns=['Gender'], dtype=int)

    print("\nAfter One-Hot Encoding :")
    print(df)

    # --------------------------------------------------
    # Q3. Group students by gender and calculate average marks
    # --------------------------------------------------

    print("\n" + border)
    print("Average Marks by Gender")
    print(border)

    # Use original gender information for grouping
    gender_data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82],
        'Gender': ['Male', 'Male', 'Female']
    }

    gender_df = pd.DataFrame(gender_data)

    average_marks = gender_df.groupby('Gender')[
        ['Math', 'Science', 'English']
    ].mean()

    print(average_marks)

    # --------------------------------------------------
    # Q4. Pie chart of subject marks for Sagar
    # --------------------------------------------------

    print("\n" + border)
    print("Pie Chart of Sagar's Subject Marks")
    print(border)

    Sagar = gender_df[gender_df['Name'] == 'Sagar']

    subjects = ['Math', 'Science', 'English']

    marks = [
        Sagar['Math'].values[0],
        Sagar['Science'].values[0],
        Sagar['English'].values[0]
    ]

    plt.figure(figsize=(7, 7))

    plt.pie(
        marks,
        labels=subjects,
        autopct='%1.1f%%'
    )

    plt.title("Sagar's Subject Marks")

    plt.show()

    # --------------------------------------------------
    # Q5. Add Status column
    # --------------------------------------------------

    print("\n" + border)
    print("Add Status Column")
    print(border)

    gender_df['Total'] = (
        gender_df['Math'] +
        gender_df['Science'] +
        gender_df['English']
    )

    gender_df['Status'] = gender_df['Total'].apply(
        lambda x: 'Pass' if x >= 250 else 'Fail'
    )

    print(gender_df)

    # --------------------------------------------------
    # Q6. Count how many students passed
    # --------------------------------------------------

    print("\n" + border)
    print("Count Passed Students")
    print(border)

    passed_students = (gender_df['Status'] == 'Pass').sum()

    print("Number of Students Passed :", passed_students)

    # --------------------------------------------------
    # Q7. Export final DataFrame to CSV file
    # --------------------------------------------------

    print("\n" + border)
    print("Export Final DataFrame to CSV")
    print(border)

    gender_df.to_csv(
        "student_final.csv",
        index=False
    )

    print("Final DataFrame exported successfully.")
    print("File Name : student_final.csv")

    # --------------------------------------------------
    # Q8. Histogram of Math Marks
    # --------------------------------------------------

    print("\n" + border)
    print("Histogram of Math Marks")
    print(border)

    plt.figure(figsize=(8, 5))

    plt.hist(
        gender_df['Math'],
        bins=3,
        edgecolor='black'
    )

    plt.title("Histogram of Math Marks")
    plt.xlabel("Math Marks")
    plt.ylabel("Number of Students")

    plt.show()

    # --------------------------------------------------
    # Q9. Rename Math column to Mathematics
    # --------------------------------------------------

    print("\n" + border)
    print("Rename Math Column to Mathematics")
    print(border)

    gender_df.rename(
        columns={'Math': 'Mathematics'},
        inplace=True
    )

    print(gender_df)

    # --------------------------------------------------
    # Q10. Boxplot for English Marks
    # --------------------------------------------------

    print("\n" + border)
    print("Boxplot for English Marks")
    print(border)

    plt.figure(figsize=(7, 5))

    plt.boxplot(gender_df['English'])

    plt.title("Boxplot of English Marks")
    plt.ylabel("English Marks")

    plt.show()

    


def main():
    MarvellousDataFrame()


if __name__ == "__main__":
    main()