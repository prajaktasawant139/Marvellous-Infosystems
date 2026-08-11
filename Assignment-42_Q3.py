import math


def MarvellousEucDistance(P1, P2):

    Ans = math.sqrt(
        (P1['StudyHours'] - P2['StudyHours']) ** 2 +
        (P1['Attendance'] - P2['Attendance']) ** 2
    )

    return Ans


def MarvellousKNNClassifier(K, Data, new_student):

    border = "-" * 50

    # Calculate Distance

    for d in Data:

        d['distance'] = MarvellousEucDistance(
            d,
            new_student
        )

    print(border)
    print("Distances of all students :")
    print(border)

    for d in Data:

        print(
            "Study Hours:",
            d['StudyHours'],
            "Attendance:",
            d['Attendance'],
            "Result:",
            d['Result'],
            "Distance:",
            round(d['distance'], 2)
        )

    # Sort Data

    sorted_data = sorted(
        Data,
        key=lambda item: item['distance']
    )

    print(border)
    print("Sorted data :")
    print(border)

    for d in sorted_data:

        print(
            "Study Hours:",
            d['StudyHours'],
            "Attendance:",
            d['Attendance'],
            "Result:",
            d['Result'],
            "Distance:",
            round(d['distance'], 2)
        )

    # Select nearest K members

    nearest = sorted_data[:K]

    print(border)
    print("Nearest", K, "members are :")
    print(border)

    for d in nearest:

        print(
            "Study Hours:",
            d['StudyHours'],
            "Attendance:",
            d['Attendance'],
            "Result:",
            d['Result']
        )

    # Voting

    votes = {}

    for neighbours in nearest:

        result = neighbours['Result']

        votes[result] = votes.get(result, 0) + 1

    print(border)
    print("Voting Result is :")
    print(border)

    for d in votes:

        print(
            "Name:",
            d,
            "Number of votes:",
            votes[d]
        )

    # Find Maximum Votes

    iMax = 0
    Name = ""

    for d in votes:

        if votes[d] > iMax:

            iMax = votes[d]
            Name = d

    return Name


def main():

    border = "-" * 50

    print(border)
    print("Marvellous Student KNN Classifier")
    print(border)

    # Dataset

    Data = [
        {
            'StudyHours': 2,
            'Attendance': 60,
            'Result': 'Fail'
        },

        {
            'StudyHours': 5,
            'Attendance': 80,
            'Result': 'Pass'
        },

        {
            'StudyHours': 6,
            'Attendance': 85,
            'Result': 'Pass'
        },

        {
            'StudyHours': 1,
            'Attendance': 50,
            'Result': 'Fail'
        }
    ]

    print("Dataset")
    print(border)

    for i in Data:

        print(i)

    print(border)

    # Step1 : Accept Student Details

    print("Step1 : Accept Student Details")
    print(border)

    StudyHours = float(
        input("Enter Study Hours: ")
    )

    Attendance = float(
        input("Enter Attendance: ")
    )

    new_student = {
        'StudyHours': StudyHours,
        'Attendance': Attendance
    }

    print(border)

    # Step2 : Apply KNN Algorithm

    print("Step2 : Apply KNN Algorithm")
    print(border)

    K = 3

    Name = MarvellousKNNClassifier(
        K,
        Data,
        new_student
    )

    # Step3 : Display Prediction

    print(border)
    print("Step3 : Final Prediction")
    print(border)

    print("K =", K)

    print(
        "Predicted Result :",
        Name
    )

    print(border)

    if Name == "Pass":

        print("Student will PASS")

    else:

        print("Student will FAIL")

    print(border)


if __name__ == "__main__":
    main()