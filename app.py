import streamlit as st
from google import genai

st.title("💪 MESA FitBuddy")
st.subheader("AI Fitness Plan Generator")

age = st.number_input("Age", min_value=13, max_value=100, value=18)
weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=60)
height = st.number_input("Height (cm)", min_value=100, max_value=220, value=165)

goal = st.selectbox(
    "Fitness Goal",
    ["General Fitness", "Strength", "Improve Stamina"]
)

diet = st.selectbox(
    "Diet Preference",
    ["Vegetarian", "Non-Vegetarian", "Eggitarian"]
)

if st.button("Generate Fitness Plan"):
    st.success("Your personalized plan will be generated using Gemini AI.")
