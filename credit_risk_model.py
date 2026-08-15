# Credit Risk Classification System
# Machine Learning using Random Forest

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Step 1: Load Dataset
data = pd.read_csv("german_credit_data.csv")

print("Credit Risk Classification System")
print("----------------------------------")


# Step 2: Remove Unnecessary Column
if "Unnamed: 0" in data.columns:
    data = data.drop("Unnamed: 0", axis=1)


# Step 3: Handle Missing Values
for column in data.columns:
    if data[column].dtype == "object":
        data[column] = data[column].fillna(data[column].mode()[0])
    else:
        data[column] = data[column].fillna(data[column].median())


# Step 4: Convert Categorical Data into Numbers
encoder = LabelEncoder()

for column in data.select_dtypes(include="object").columns:
    data[column] = encoder.fit_transform(data[column])


# Step 5: Separate Input and Output
X = data.drop("Risk", axis=1)
y = data["Risk"]


# Step 6: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Step 7: Create Random Forest Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Step 8: Train the Model
model.fit(X_train, y_train)


# Step 9: Make Predictions
y_pred = model.predict(X_test)


# Step 10: Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")


# Step 11: Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))