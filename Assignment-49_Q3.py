import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    data = np.array([
        [25, 20000],
        [30, 40000],
        [35, 80000]
    ])

    print("Original Dataset:")
    print(data)

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(data)

    print("\nScaled Dataset:")
    print(scaled_data)

if __name__ == "__main__":
    main()