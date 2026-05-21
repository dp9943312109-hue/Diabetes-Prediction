import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
#Load the dataset
data pd.read_csv('diabetes.csv')
#Split data into features (X) and target (y)
X data.drop('Outcome', axis-1)
V data['Outcome']
#Split the data into training and testing sets
X train, X test, y train, y test train test split(X, y, tesc size=0.3, random
state-42)
#Initialize and train the Logistic Regression model
model LogisticRegression (max iter=1000)
model.fit (X train, y train)
#Streamlit App Interface
st.title("Diabetes Prediction App")
st.write("Enter the following details to predict the likelihood of diabetes.")
#User Inputs for prediction
input data = []
for col in X.columns:
value st.number_input (f"Enter (col)", min_value-0.0, step-0.1)
input data.append(value)
#Predict button
if st.button("Predict"):
prediction = model.predict([input_data])
result "Diabetic" if prediction [0] 1 else "Non-Diabetic"
st.success(f"Prediction: {result}")
#Model performance metrics
st.supheader("Model Performance")
y pred model.predict (X_test)
accuracy accuracy score (y test, y pred)
st.write("Accuracy: (accuracy:.2}")
st.text("Classification Report:")
st.text(classification_report (y test, y_pred))
