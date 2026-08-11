import math


def MarvellousEucDistance(P1, P2):

    Ans = math.sqrt(
        (P1['X'] - P2['X']) ** 2 +
        (P1['Y'] - P2['Y']) ** 2
    )

    return Ans


def MarvellousKNNClassifier(K, Data, new_point):

    border = "-" * 50

    # Calculate Distance

    for d in Data:

        d['distance'] = MarvellousEucDistance(
            d,
            new_point
        )

    # Sort Data

    sorted_data = sorted(
        Data,
        key=lambda item: item['distance']
    )

    # Select Nearest K Members

    nearest = sorted_data[:K]

    print(border)
    print("Nearest", K, "members are :")
    print(border)

    for d in nearest:

        print(
            d['point'],
            "Distance:",
            round(d['distance'], 2),
            "Label:",
            d['label']
        )

    # Voting

    votes = {}

    for neighbours in nearest:

        label = neighbours['label']

        votes[label] = votes.get(label, 0) + 1

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

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'},
        {'point': 'E', 'X': 5, 'Y': 4, 'label': 'Blue'}
    ]

    print(border)
    print("Marvellous KNN - Effect of K")
    print(border)

    print("Dataset")
    print(border)

    for i in Data:

        print(i)

    print(border)

    # Accept New Point

    print("Enter New Point")
    print(border)

    X = float(input("Enter X coordinate: "))
    Y = float(input("Enter Y coordinate: "))

    new_point = {
        'X': X,
        'Y': Y
    }

    # --------------------------------------------------
    # K = 1
    # --------------------------------------------------

    print(border)
    print("K = 1")
    print(border)

    Name1 = MarvellousKNNClassifier(
        1,
        Data,
        new_point
    )

    print("Prediction for K = 1 :", Name1)

    # --------------------------------------------------
    # K = 3
    # --------------------------------------------------

    print(border)
    print("K = 3")
    print(border)

    Name3 = MarvellousKNNClassifier(
        3,
        Data,
        new_point
    )

    print("Prediction for K = 3 :", Name3)

    # --------------------------------------------------
    # K = 5
    # --------------------------------------------------

    print(border)
    print("K = 5")
    print(border)

    Name5 = MarvellousKNNClassifier(
        5,
        Data,
        new_point
    )

    print("Prediction for K = 5 :", Name5)

    # --------------------------------------------------
    # Final Result
    # --------------------------------------------------

    print(border)
    print("Final Result")
    print(border)

    print("K = 1 :", Name1)
    print("K = 3 :", Name3)
    print("K = 5 :", Name5)

    # --------------------------------------------------
    # Why does prediction change?
    # --------------------------------------------------

    print(border)
    print("Why does the prediction changes when K increases?")
    print(border)

    print(
        "The prediction changes when K increases because"
    )

    print(
        "different numbers of nearest neighbours are"
    )

    print(
        "considered for voting."
    )

    print(
        "For small K, the prediction depends mainly on"
    )

    print(
        "the closest points."
    )

    print(
        "For larger K, more points participate in voting,"
    )

    print(
        "so the majority class can change."
    )

    print(border)


if __name__ == "__main__":
    main()