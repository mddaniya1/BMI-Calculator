import streamlit as st

# Title and description
st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) based on your weight and height.")

# Input fields
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, step=0.1, format="%.1f")
height = st.number_input("Enter your height (in meters):", min_value=0.0, step=0.01, format="%.2f")

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is **{bmi:.2f}**.")
        
        # BMI Categories
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than 0.")




