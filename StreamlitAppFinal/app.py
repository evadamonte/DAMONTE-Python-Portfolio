import streamlit as st
from PIL import Image
import os

# Set page config
st.set_page_config(page_title="Fitness Goal Tracker", page_icon="💪", layout="centered")

# Display a hero image
st.image("https://images.unsplash.com/photo-1583454110551-21c3e7f42b37?fit=crop&w=1200&q=80", use_column_width=True)

# Try loading your personal photo
try:
    image = Image.open("StreamlitAppFinal/my_photo.jpg")
    rotated_image = image.rotate(-90, expand=True)
    st.sidebar.image(rotated_image, use_column_width=True)
except:
    st.sidebar.warning("Personal image not found. Using app default visuals.")

# App title and intro
st.title("💪 Fitness Goal Tracker")
st.markdown(
    "<h4 style='color: #4CAF50;'>Plan smarter. Train better. Eat cleaner.</h4>",
    unsafe_allow_html=True,
)
st.write("Enter your information below to receive a personalized fitness and nutrition plan tailored to your goals.")

# Input section
st.markdown("### 📋 Your Info:")
weight = st.number_input("Current weight (lbs):", min_value=50, max_value=500)
goal_weight = st.number_input("Goal weight (lbs):", min_value=50, max_value=500)

# New height input (feet and inches)
height_feet = st.number_input("Height (feet):", min_value=3, max_value=8)
height_inches = st.number_input("Additional height (inches):", min_value=0, max_value=11)
height = height_feet * 12 + height_inches

age = st.number_input("Age:", min_value=10, max_value=100)
activity_level = st.selectbox("Activity level:", ["Sedentary", "Lightly Active", "Active", "Very Active"])
goal_type = st.selectbox("What is your goal?", ["Lose weight", "Maintain", "Gain muscle"])

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏋️ Workout Plan", "🥗 Nutrition Plan", "🎤 Motivation", "🎵 Workout Music"])

# Generate Plan Button
if st.button("Generate My Plan"):
    # Basic input validation
    if weight == 0 or goal_weight == 0 or height == 0 or age == 0:
        st.error("🚫 Please make sure all input fields are filled out correctly before generating your plan.")
    else:
        # BMI calculation
        bmi = (weight / (height * height)) * 703
        st.subheader(f"Your BMI is: {bmi:.1f}")
        if bmi < 18.5:
            bmi_status = "Underweight"
            st.info("You are underweight.")
        elif bmi < 24.9:
            bmi_status = "Healthy Weight"
            st.success("You are at a healthy weight.")
        elif bmi < 29.9:
            bmi_status = "Overweight"
            st.warning("You are overweight.")
        else:
            bmi_status = "Obese"
            st.error("You are obese.")

        # Calorie estimation
        bmr = 10 * (weight * 0.45) + 6.25 * (height * 2.54) - 5 * age + 5
        multiplier = {"Sedentary": 1.2, "Lightly Active": 1.375, "Active": 1.55, "Very Active": 1.725}
        maintenance_calories = bmr * multiplier[activity_level]
        goal_calories = maintenance_calories + (-500 if goal_type == "Lose weight" else 300 if goal_type == "Gain muscle" else 0)
        st.subheader(f"Recommended Daily Calories: {int(goal_calories)} kcal")

        # Download plan text
        plan_text = f"""Fitness Goal Tracker Plan
------------------------------
Current Weight: {weight} lbs
Goal Weight: {goal_weight} lbs
Height: {height_feet} ft {height_inches} in ({height} inches)
Age: {age}
Activity Level: {activity_level}
Goal Type: {goal_type}
BMI: {bmi:.1f} ({bmi_status})
Recommended Calories: {int(goal_calories)} kcal
"""

        with tab1:
            st.header("🏋️ Your Weekly Workout Plan")
            if goal_type == "Lose weight":
                plan = """
                - 5x Brisk walks (30 mins)
                - 2x Strength circuits
                - 1x HIIT cardio session
                """
            elif goal_type == "Gain muscle":
                plan = """
                - 4x Strength (Push, Pull, Legs, Upper Split)
                - 1x Conditioning (sleds, rowing)
                """
            else:
                plan = """
                - 3x Full-body lifts
                - 2x Light cardio (cycling, jogging)
                """
            st.markdown(plan)
            plan_text += "\nWorkout Plan:\n" + plan.replace("-", "*")

        with tab2:
            st.header("🥗 Your Nutrition Guide")
            nutrition = """
            **Focus on:**
            - Protein: Chicken, eggs, tofu, legumes
            - Carbs: Brown rice, oats, quinoa
            - Fats: Avocado, olive oil, almonds

            **Sample Meals:**

            🍽️ Protein Smoothie  
            🍳 Veggie Omelet  
            🥗 Chicken Power Bowl  
            """
            st.markdown(nutrition)
            plan_text += "\nNutrition Plan:\n" + nutrition.replace("**", "").replace("-", "*")

        with tab3:
            st.header("🔥 Motivational Speeches")
            st.write("Need a boost? These short speeches will get your mindset right.")
            st.markdown("**1. Eric Thomas – 'How Bad Do You Want It?'**")
            st.video("https://www.youtube.com/watch?v=lsSC2vx7zFQ")
            st.markdown("**2. Jocko Willink – 'GOOD'**")
            st.video("https://www.youtube.com/watch?v=IdTMDpizis8")
            st.markdown("**3. Les Brown – 'You Gotta Be Hungry'**")
            st.video("https://www.youtube.com/watch?v=KxGRhd_iWuE")

        with tab4:
            st.header("🎵 Choose Your Workout Music")
            workout_type = st.selectbox("What type of workout are you doing?", ["Yoga 🧘", "Jogging 🏃", "Weight Lifting 🏋️"])

            if workout_type == "Yoga 🧘":
                st.markdown("**Relaxing Yoga Playlist**")
                st.components.v1.iframe("https://open.spotify.com/embed/playlist/37i9dQZF1DWUZ5bk6qqDSy", height=380)
            elif workout_type == "Jogging 🏃":
                st.markdown("**Running Motivation Playlist**")
                st.components.v1.iframe("https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC", height=380)
            else:
                st.markdown("**Hardcore Lifting Playlist**")
                st.components.v1.iframe("https://open.spotify.com/embed/playlist/37i9dQZF1DWUVpAXiEPK8P", height=380)

        # Provide download button
        st.subheader("📥 Download Your Custom Plan:")
        st.download_button("Download My Plan", plan_text, "fitness_plan.txt", "text/plain")
