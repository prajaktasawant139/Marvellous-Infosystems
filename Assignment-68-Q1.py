# Input Image (5x5)
image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Kernel (3x3 edge detection)
kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

# Output feature map size = (5-3+1) x (5-3+1) = 3x3
feature_map = []

# Perform convolution
for i in range(3):  # rows
    row = []
    for j in range(3):  # columns
        sum_val = 0
        print(f"\nRegion at position ({i},{j}):")

        # Extract 3x3 region and multiply
        for m in range(3):
            for n in range(3):
                val = image[i + m][j + n]
                k = kernel[m][n]
                mul = val * k
                sum_val += mul
                print(f"{val}*{k}", end="  ")
            print()

        print("Sum =", sum_val)
        row.append(sum_val)
    feature_map.append(row)

# Print final feature map
print("\nFinal Feature Map:")
for r in feature_map:
    print(r)