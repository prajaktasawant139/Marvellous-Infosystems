# Deep Learning Assignment
# Create a neural network model to predict loan approval

import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# ============================================================
# 1. CREATE DATASET
# ============================================================

# Features:
# [Applicant Income, Credit Score, Loan Amount,
#  Existing EMI, Employment Status]

X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 150000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 1000, 0],
    [70000, 780, 600000, 10000, 1]
])

# Output:
# 0 = Loan rejected
# 1 = Loan approved

y = np.array([
    0, 1, 1, 0, 1,
    1, 0, 1, 0, 1
])

print("=" * 60)
print("DATASET")
print("=" * 60)

print("X :")
print(X)

print("\ny :")
print(y)

# ============================================================
# 2. PREPROCESS CATEGORICAL VALUES
# ============================================================

# Employment Status is already encoded:
# 0 = Not Stable
# 1 = Stable

print("\n" + "=" * 60)
print("CATEGORICAL VALUE ENCODING")
print("=" * 60)

print("Employment Status:")
print("0 = Not Stable")
print("1 = Stable")

# ============================================================
# 3. SPLIT DATASET
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ============================================================
# 4. APPLY STANDARD SCALER
# ============================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ============================================================
# 5. CREATE FNN MODEL
# ============================================================

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(5,)),
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(5, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("\n" + "=" * 60)
print("FNN MODEL")
print("=" * 60)

model.summary()

# ============================================================
# 6. TRAIN FNN MODEL
# ============================================================

model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=4,
    verbose=0
)

# ============================================================
# 7. EVALUATE MODEL
# ============================================================

loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

print("Test Loss     :", loss)
print("Test Accuracy :", accuracy * 100, "%")

# ============================================================
# 8. PREDICT APPROVAL FOR NEW APPLICANT
# ============================================================

# Assignment Test Input:
# [Applicant Income, Credit Score, Loan Amount,
#  Existing EMI, Employment Status]

new_applicant = np.array([
    [55000, 720, 400000, 10000, 1]
])

# Apply the same scaler
new_applicant_scaled = scaler.transform(new_applicant)

# Predict
prediction = model.predict(
    new_applicant_scaled,
    verbose=0
)

# ============================================================
# 9. DISPLAY PREDICTION
# ============================================================

print("\n" + "=" * 60)
print("NEW APPLICANT PREDICTION")
print("=" * 60)

print("New Applicant :", new_applicant[0])

print("Prediction Probability :", prediction[0][0])

if prediction[0][0] >= 0.5:
    print("Prediction : 1")
    print("Result : Loan Approved")
else:
    print("Prediction : 0")
    print("Result : Loan Rejected")