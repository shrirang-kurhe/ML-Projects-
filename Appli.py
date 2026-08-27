import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("C:\\Users\\admin\\Data Science - shrirang Sir\\Machine Learning\\Supervised Learning Projects\\Ensamble Learning\\Random Forest Project\\random_forest_regressor.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("Random Forest Regression App")
st.write("Enter employee details to predict the target value.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=70, value=25)

experience = st.number_input(
    "Experience (Years)",
    min_value=0,
    max_value=40,
    value=2
)

education = st.number_input(
    "Education (Years)",
    min_value=5,
    max_value=25,
    value=16
)

hours = st.number_input(
    "Hours Per Week",
    min_value=1,
    max_value=100,
    value=40
)

projects = st.number_input(
    "Projects Completed",
    min_value=0,
    max_value=100,
    value=5
)

certifications = st.number_input(
    "Certifications",
    min_value=0,
    max_value=20,
    value=2
)

performance = st.number_input(
    "Performance Score",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

# Prediction button
if st.button("Predict"):

    # Create input array
    input_data = np.array([[
        age,
        experience,
        education,
        hours,
        projects,
        certifications,
        performance
    ]])

    # Prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(f"Predicted Value: {prediction[0]:.2f}")