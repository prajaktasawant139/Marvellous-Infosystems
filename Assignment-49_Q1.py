import numpy as np

def main():
    data = np.array([6, 7, 8, 9, 10, 11, 12])

    mean = np.mean(data)

    print("Dataset :", data)
    print("Mean :", mean)

if __name__ == "__main__":
    main()