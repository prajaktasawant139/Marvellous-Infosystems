# Deep Learning Assignment
# Create a neural network model to predict whether a customer will leave a service

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# ============================================================
# 1. CREATE DATASET
# ============================================================

# Features:
# [Age, Monthly Charges, Tenure, Complaints, Support Calls]

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

# Output:
# 0 = Customer will stay
# 1 = Customer will leave

y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
])

print("=" * 60)
print("DATASET")
print("=" * 60)

print("X :")
print(X)

print("\ny :")
print(y)

# ============================================================
# 2. CLEAN THE DATASET
# ============================================================

print("\n" + "=" * 60)
print("CLEAN DATASET")
print("=" * 60)

print("Missing values in X :", np.isnan(X).sum())
print("Missing values in y :", np.isnan(y).sum())

# ============================================================
# 3. SPLIT THE DATASET
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ============================================================
# 4. APPLY STANDARDSCALER
# ============================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ============================================================
# 5. CREATE FNN MODEL
# ============================================================

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu", input_shape=(5,)),
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
    verbose=0
)

# ============================================================
# 7. EVALUATE ACCURACY
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
print("Test Accuracy :", accuracy)

# ============================================================
# 8. TEST INPUT
# ============================================================

new_customer = np.array([
    [46, 1450, 5, 6, 9]
])

# Apply the same scaler
new_customer_scaled = scaler.transform(new_customer)

# Predict
prediction = model.predict(
    new_customer_scaled,
    verbose=0
)

# Convert probability into class
if prediction[0][0] >= 0.5:
    result = 1
    message = "Customer may leave"
else:
    result = 0
    message = "Customer may stay"

# ============================================================
# 9. DISPLAY PREDICTION
# ============================================================

print("\n" + "=" * 60)
print("PREDICTION")
print("=" * 60)

print("New Customer :", new_customer[0])
print("Prediction Probability :", prediction[0][0])
print("Prediction :", result)
print("Result :", message)