import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the data
loan_data = pd.read_csv("loan_data.csv")

# Prepare the data
X = loan_data.drop(columns=["Default"])
y = loan_data["Default"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Function to predict the probability of default for a new loan
def predict_default_probability(loan_details):
    default_probability = model.predict_proba([loan_details])[0][1]
    return default_probability

# Example usage
new_loan = [50000, 10000, 35, 1, 0]  # Income, Total loans outstanding, Age, Employment status, Previous default
expected_loss = predict_default_probability(new_loan) * 0.10  # Assuming recovery rate of 10%
print("Expected loss on the loan:", expected_loss)
