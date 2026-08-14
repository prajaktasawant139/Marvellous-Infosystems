import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def MarvellousDataFrame():
    border = "-" * 50

    # Q1. Create DataFrame for student marks
    print(border)
    print("Create DataFrame")
    print(border)

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    print("Student DataFrame :")
    print(df)

    print(border)
    print("Shape :", df.shape)

    print(border)
    print("Columns :", df.columns.tolist())

    print(border)
    print("Data Types :")
    print(df.dtypes)

    # Q2. Descriptive statistics
    print("\n" + border)
    print("Descriptive Statistics")
    print(border)

    print(df.describe())

    # Q3. Add Total column
    print("\n" + border)
    print("Add Total Column")
    print(border)

    df['Total'] = df['Math'] + df['Science'] + df['English']

    print(df)

    # Q4. Students who scored more than 85 in Science
    print("\n" + border)
    print("Students who scored more than 85 in Science")
    print(border)

    result = df[df['Science'] > 85]

    print(result)

    # Q5. Replace Pooja with Puja
    print("\n" + border)
    print("Replace Pooja with Puja")
    print(border)

    df['Name'] = df['Name'].replace('Pooja', 'Puja')

    print(df)

    # Q6. Sort DataFrame by Total in descending order
    print("\n" + border)
    print("Sort DataFrame by Total in Descending Order")
    print(border)

    sorted_df = df.sort_values(by='Total', ascending=False)

    print(sorted_df)

    # Q7. Bar plot of student names vs Total marks
    print("\n" + border)
    print("Bar Plot of Student Names vs Total Marks")
    print(border)

    plt.figure(figsize=(8, 5))

    plt.bar(df['Name'], df['Total'])

    plt.title("Student Names vs Total Marks")
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")

    plt.show()

    # Q8. Line chart of Amit's marks
    print("\n" + border)
    print("Line Chart of Amit's Marks")
    print(border)

    amit = df[df['Name'] == 'Amit']

    subjects = ['Math', 'Science', 'English']
    marks = [
        amit['Math'].values[0],
        amit['Science'].values[0],
        amit['English'].values[0]
    ]

    plt.figure(figsize=(8, 5))

    plt.plot(subjects, marks, marker='o')

    plt.title("Amit's Marks Across All Subjects")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")

    plt.show()

    # Q9. Create DataFrame with missing values
    print("\n" + border)
    print("DataFrame with Missing Values")
    print(border)

    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }

    df2 = pd.DataFrame(data2)

    print("DataFrame with Missing Values :")
    print(df2)

    print(border)
    print("DataFrame after filling missing values with column mean :")

    df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
    df2['Science'] = df2['Science'].fillna(df2['Science'].mean())

    print(df2)

    # Q10. Drop English column from original DataFrame
    print("\n" + border)
    print("Drop English Column")
    print(border)

    df = df.drop('English', axis=1)

    print(df)

    print(border)


def main():
    MarvellousDataFrame()


if __name__ == "__main__":
    main()