import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    data = np.array([
        [25, 20000],
        [30, 40000],
        [35, 80000]
    ])

    # Select two points
    point1 = data[0]
    point2 = data[1]

    print("Point 1 :", point1)
    print("Point 2 :", point2)

    # Calculate Euclidean distance before scaling
    distance_before = np.linalg.norm(point1 - point2)

    print("\nEuclidean Distance Before Scaling :", distance_before)

    # Apply feature scaling
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Select scaled points
    scaled_point1 = scaled_data[0]
    scaled_point2 = scaled_data[1]

    print("\nScaled Point 1 :", scaled_point1)
    print("Scaled Point 2 :", scaled_point2)

    # Calculate Euclidean distance after scaling
    distance_after = np.linalg.norm(scaled_point1 - scaled_point2)

    print("\nEuclidean Distance After Scaling :", distance_after)

    # Calculate difference
    difference = abs(distance_before - distance_after)

    print("\nDifference in Distance :", difference)

    print("\nExplanation:")
    print("Before scaling, the salary feature has much larger values than age.")
    print("Therefore, salary has a greater influence on the Euclidean distance.")
    print("After scaling, both features are converted to a comparable scale.")
    print("Therefore, the influence of salary is reduced and the distance changes.")

if __name__ == "__main__":
    main()