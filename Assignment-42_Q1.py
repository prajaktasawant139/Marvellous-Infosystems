import math


def MarvellousEucDistance(P1, P2):

    Ans = math.sqrt(
        (P1["X"] - P2["X"]) ** 2 +
        (P1["Y"] - P2["Y"]) ** 2
    )

    return Ans


def MarvellousKNNClassifier():

    border = "-" * 50

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    print("Dataset")
    print(border)

    for i in Data:
        print(i)

    print(border)

    # Step1 : Accept X and Y coordinates of new point

    print("Step1 : Accept X and Y coordinates of new point")
    print(border)

    X = float(input("Enter X coordinate: "))
    Y = float(input("Enter Y coordinate: "))

    new_point = {
        'X': X,
        'Y': Y
    }

    print(border)

    # Step2 : Calculate Euclidean distance

    print("Step2 : Calculate Euclidean distance")
    print(border)

    for d in Data:

        d['distance'] = MarvellousEucDistance(
            d,
            new_point
        )

        print(
            d['point'],
            "- Distance:",
            round(d['distance'], 2),
            "- Label:",
            d['label']
        )

    print(border)

    # Step3 : Sort the distances

    print("Step3 : Sort the distances")
    print(border)

    sorted_data = sorted(
        Data,
        key=lambda item: item['distance']
    )

    print("Sorted data :")

    for d in sorted_data:

        print(
            d['point'],
            "- Distance:",
            round(d['distance'], 2),
            "- Label:",
            d['label']
        )

    print(border)

    # Step4 : Select K = 3 nearest neighbours

    print("Step4 : Select K = 3 nearest neighbours")
    print(border)

    K = 3

    nearest = sorted_data[:K]

    print("Nearest Neighbours :")

    for d in nearest:

        print(
            d['point'],
            "- Distance:",
            round(d['distance'], 2),
            "- Label:",
            d['label']
        )

    print(border)

    # Step5 : Majority Voting

    print("Step5 : Majority Voting")
    print(border)

    votes = {}

    for neighbours in nearest:

        label = neighbours['label']

        votes[label] = votes.get(label, 0) + 1

    print("Voting Result is :")
    print(border)

    for d in votes:

        print(
            "Name:",
            d,
            "Number of votes:",
            votes[d]
        )

    print(border)

    iMax = 0
    Name = ""

    for d in votes:

        if votes[d] > iMax:

            iMax = votes[d]
            Name = d

    print("Predicted Class:", Name)

    print(border)


def main():

    MarvellousKNNClassifier()


if __name__ == "__main__":
    main()