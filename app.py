import streamlit as st
import joblib
import numpy as np

# Load the model and scaler
scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')

# App UI
st.title('Churn Prediction App')
st.divider()
st.write('Please enter the values and hit the predict button for getting a prediction')
st.divider()

# Inputs
age = st.number_input('Enter age', min_value=10, max_value=100, value=30)
tenure = st.number_input('Enter tenure', min_value=0, max_value=130, value=10)
monthly_charge = st.number_input('Enter monthly charge', min_value=30, max_value=150)
gender = st.selectbox('Enter the gender', ['Male', 'Female'])

# Gender encoding logic
gender_selected = 1 if gender == 'Female' else 0

# Prediction button
predict_button = st.button('Predict')

if predict_button:
    st.divider()
    st.balloons()
    
    # Preparing input array
    X = [age, gender_selected, tenure, monthly_charge]

    X1 = np.array(X)
    X_array = scaler.transform([X1])

    # Model prediction
    prediction = model.predict(X_array)[0]
    result = 'Yes' if prediction == 1 else 'No'

    st.write(f'Predicted: {result}')
else:
    st.write('Please enter the values and use the predict button')