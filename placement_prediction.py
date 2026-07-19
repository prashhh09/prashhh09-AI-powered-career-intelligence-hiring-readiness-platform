import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset

df = pd.read_csv("placement_data.csv")

# Features

X = df[[
    "cgpa",
    "skills",
    "certifications",
    "projects"
]]

# Target

y = df["placed"]

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model

model = LogisticRegression()

model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)

print(
    "Model Accuracy:",
    round(accuracy * 100, 2),
    "%"
)

print("Model Trained Successfully!")

# User Input

cgpa = float(input("Enter CGPA: "))
skills = int(input("Number of Skills: "))
certifications = int(input("Number of Certifications: "))
projects = int(input("Number of Projects: "))

prediction = model.predict(
    [[cgpa, skills, certifications, projects]]
)

probability = model.predict_proba(
    [[cgpa, skills, certifications, projects]]
)

print("\n===== PLACEMENT PREDICTION =====")

if prediction[0] == 1:
    print("Likely to Get Placed")
else:
    print("Placement Risk")

print(
    "Placement Probability:",
    round(probability[0][1] * 100, 2),
    "%"
)