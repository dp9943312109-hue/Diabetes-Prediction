import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv('diabetes.csv')

# Features and target
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Streamlit App
st.title("Diabetes Prediction App")
st.write("Enter patient details below")

# User input
input_data = []

for col in X.columns:
    value = st.number_input(f"Enter {col}", min_value=0.0, step=0.1)
    input_data.append(value)

# Prediction button
if st.button("Predict"):

    prediction = model.predict([input_data])

    if prediction[0] == 1:
        st.error("Patient is Diabetic")
    else:
        st.success("Patient is Non-Diabetic")

# Accuracy
st.subheader("Model Performance")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

st.write(f"Accuracy: {accuracy:.2f}")

st.text(classification_report(y_test, y_pred))
