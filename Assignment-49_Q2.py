import numpy as np

def main():
    data = np.array([6, 7, 8, 9, 10, 11, 12])

    variance = np.var(data)
    standard_deviation = np.std(data)

    print("Dataset :", data)
    print("Variance :", variance)
    print("Standard Deviation :", standard_deviation)

if __name__ == "__main__":
    main()