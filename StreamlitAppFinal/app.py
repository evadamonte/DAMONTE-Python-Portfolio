import streamlit as st
from PIL import Image
import os

# Set page config
st.set_page_config(page_title="Fitness Goal Tracker", page_icon="💪", layout="centered")

# Try loading your personal photo
try:
    image = Image.open("my_photo.jpg")
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
location_type = st.selectbox("Preferred workout location:", ["At Home", "Outdoor", "Gym"])

# Animated Progress Bars
if height > 0:
    bmi = (weight / (height * height)) * 703
    st.progress(min(int((bmi / 40) * 100), 100), text=f"Current BMI: {bmi:.1f}")
    cal_bar = int((weight / 300) * 100)
    st.progress(min(cal_bar, 100), text=f"Weight Progress: {weight} lbs")

# Tabs
workout_tab, nutrition_tab, motivation_tab, music_tab = st.tabs(["🏋️ Workout Plan", "🥗 Nutrition Plan", "🎤 Motivation", "🎵 Workout Music"])

# Tab 3: Motivation
with motivation_tab:
    st.header("🔥 Motivational Speeches")
    st.write("Need a boost? These short speeches will get your mindset right.")
    st.markdown("**1. Eric Thomas – 'How Bad Do You Want It?'**")
    st.video("https://www.youtube.com/watch?v=lsSC2vx7zFQ")
    st.markdown("**2. Jocko Willink – 'GOOD'**")
    st.video("https://www.youtube.com/watch?v=IdTMDpizis8")
    st.markdown("**3. Les Brown – 'You Gotta Be Hungry'**")
    st.video("https://www.youtube.com/watch?v=KxGRhd_iWuE")

# Tab 4: Music
with music_tab:
    st.header("🎵 Choose Your Workout Music")
    playlist_options = {
        "Yoga 🧘": "https://open.spotify.com/embed/playlist/37i9dQZF1DWUZ5bk6qqDSy",
        "Jogging 🏃": "https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC",
        "Weight Lifting 🏋️": "https://open.spotify.com/embed/playlist/37i9dQZF1DWUVpAXiEPK8P"
    }
    choice = st.selectbox("What type of workout are you doing?", list(playlist_options.keys()))
    st.markdown(f"**{choice} Playlist**")
    st.components.v1.iframe(playlist_options[choice], height=380)

# Generate Plan Button
if st.button("Generate My Plan"):
    if weight == 0 or goal_weight == 0 or height == 0 or age == 0:
        st.error("🚫 Please make sure all input fields are filled out correctly before generating your plan.")
    else:
        bmi = (weight / (height * height)) * 703
        st.subheader(f"Your BMI is: {bmi:.1f}")
        bmi_status = ""
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

        bmr = 10 * (weight * 0.45) + 6.25 * (height * 2.54) - 5 * age + 5
        multiplier = {"Sedentary": 1.2, "Lightly Active": 1.375, "Active": 1.55, "Very Active": 1.725}
        maintenance_calories = bmr * multiplier[activity_level]
        goal_calories = maintenance_calories + (-500 if goal_type == "Lose weight" else 300 if goal_type == "Gain muscle" else 0)
        st.subheader(f"Recommended Daily Calories: {int(goal_calories)} kcal")

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

        with workout_tab:
            st.header("🏋️ Your Personalized Weekly Workout Plan")
            st.markdown("[Click here for YouTube workout demos](https://www.youtube.com/channel/UC7t6QJ4u8qF8pI-vibX-BUQ)")
            plan = ""
            if bmi_status in ["Overweight", "Obese"]:
                if location_type == "At Home":
                    plan = """
                    - 4x Low-impact cardio (march in place, step-ups)
                    - 3x Strength (bodyweight squats, wall pushups, glute bridges)
                    - Daily stretching & mobility
                    """
                elif location_type == "Outdoor":
                    plan = """
                    - 5x Walks (start with 20 mins, add 5 mins each week)
                    - 2x Hill walks or stairs
                    - Optional: Resistance band circuits on park benches
                    """
                else:
                    plan = """
                    - 3x Elliptical or recumbent bike (20–30 mins)
                    - 2x Strength machines (leg press, row, chest press)
                    - Stretch & foam roll after each session
                    """
            elif bmi_status == "Underweight":
                if location_type == "At Home":
                    plan = """
                    - 4x Strength (push-ups, lunges, backpack rows)
                    - 2x Yoga or pilates for stability
                    - Calorie-dense post-workout snacks
                    """
                elif location_type == "Outdoor":
                    plan = """
                    - 3x Hill sprints or stair intervals
                    - 2x Full-body strength using park equipment
                    - Extra rest and high-protein meals after
                    """
                else:
                    plan = """
                    - 4x Gym weightlifting (compound lifts + accessories)
                    - 1x HIIT finishers
                    - Protein shake post-session
                    """
            else:
                if location_type == "At Home":
                    plan = """
                    - 3x Full-body HIIT (squats, pushups, planks, jumping jacks)
                    - 2x Mobility & stretching days
                    - Optional: Dumbbell or resistance band circuits
                    """
                elif location_type == "Outdoor":
                    plan = """
                    - 3x Jog or bike (30–45 mins)
                    - 2x Bodyweight circuits using park
                    - 1x Long walk or hike
                    """
                else:
                    plan = """
                    - 4x Gym split (Push/Pull/Legs/Conditioning)
                    - 1x Cardio day (rower, incline walk)
                    - Optional: group fitness class
                    """
            st.markdown(plan)
            plan_text += "\nWorkout Plan:\n" + plan.replace("-", "*")

        with nutrition_tab:
            st.header("🥗 Your Nutrition Guide")
            st.markdown("How to meal prep: https://nutritionsource.hsph.harvard.edu/meal-prep/")

            st.markdown("### 🔑 Focus On:")
            st.markdown("- **Protein:** Chicken, tofu, fish, eggs — [Recipe Ideas](https://www.bbcgoodfood.com/recipes/collection/high-protein-recipes)")
            st.markdown("- **Carbs:** Sweet potato, oats, quinoa, brown rice — [Healthy Carbs](https://www.mayoclinic.org/healthy-lifestyle/recipes/healthy-carb-recipes/rcs-20077160)")
            st.markdown("- **Fats:** Avocado, olive oil, nuts — [Healthy Fats Guide](https://palm.southbeachdiet.com/healthy-fat-servings/)")
            st.markdown("- **Vegetables:** Leafy greens, peppers, broccoli — [Vegetable Side Dishes](https://www.loveandlemons.com/vegetable-side-dishes/)")

            st.markdown("### 🍽️ Sample Meal Ideas:")
            st.markdown("- 🥤 [Protein Smoothie Recipe](https://joyfoodsunshine.com/protein-smoothie/)")
            st.markdown("- 🍳 [Veggie Omelet Recipe](https://joyfoodsunshine.com/omelette-recipe/)")
            st.markdown("- 🥗 [Chicken Power Bowl](https://ohsheglows.com/meal-prep-week-long-power-bowls/)")

            plan_text += "\nNutrition Plan:\n"
            plan_text += "Protein: Chicken, tofu, fish, eggs\n"
            plan_text += "Carbs: Sweet potato, oats, quinoa, brown rice\n"
            plan_text += "Fats: Avocado, olive oil, nuts\n"
            plan_text += "Veggies: Leafy greens, broccoli, peppers\n"
            plan_text += "Recipes: Smoothie, Omelet, Power Bowl\n"


        st.subheader("📥 Download Your Custom Plan:")
        st.download_button("Download My Plan", plan_text, "fitness_plan.txt", "text/plain")
