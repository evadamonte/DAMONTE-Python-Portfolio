import streamlit as st

# Set page configuration
st.set_page_config(page_title="Fitness Goal Tracker", page_icon="🏋️‍♂️", layout="centered")

# Display a public online image
st.sidebar.image(
    "StreamlitAppFinal/my_photo.jpg",
    use_column_width=True
)

st.title("🏋️‍♂️ Fitness Goal Tracker")
st.write("Welcome! Enter your details below to get a personalized fitness and nutrition plan tailored to your goals.")


# User Inputs
st.header("📋 Enter Your Information")
weight = st.number_input("Enter your current weight (lbs):", min_value=50, max_value=500)
goal_weight = st.number_input("Enter your goal weight (lbs):", min_value=50, max_value=500)
height = st.number_input("Enter your height (inches):", min_value=48, max_value=84)
age = st.number_input("Enter your age:", min_value=10, max_value=100)
activity_level = st.selectbox("Select your activity level:", ["Sedentary", "Lightly Active", "Active", "Very Active"])
goal_type = st.selectbox("What is your goal?", ["Lose weight", "Maintain", "Gain muscle"])

# Create Tabs
tab1, tab2 = st.tabs(["🏋️ Workout Plan", "🥗 Nutrition Plan"])

# When user clicks "Generate My Plan"
if st.button("Generate My Plan"):

    # BMI Calculation
    bmi = (weight / (height * height)) * 703
    st.subheader(f"Your BMI is: {bmi:.1f}")

    # BMI Category
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

    # Calorie Estimate
    bmr = 10 * (weight * 0.45) + 6.25 * (height * 2.54) - 5 * age + 5
    multiplier = {"Sedentary": 1.2, "Lightly Active": 1.375, "Active": 1.55, "Very Active": 1.725}
    maintenance_calories = bmr * multiplier[activity_level]

    if goal_type == "Lose weight":
        goal_calories = maintenance_calories - 500
    elif goal_type == "Gain muscle":
        goal_calories = maintenance_calories + 300
    else:
        goal_calories = maintenance_calories

    st.subheader(f"Recommended Daily Calories: {int(goal_calories)} kcal")

    # Start building the download plan text
    plan_text = f"""Fitness Goal Tracker Plan
------------------------------
Current Weight: {weight} lbs
Goal Weight: {goal_weight} lbs
Height: {height} inches
Age: {age}
Activity Level: {activity_level}
Goal Type: {goal_type}

BMI: {bmi:.1f} ({bmi_status})
Recommended Daily Calories: {int(goal_calories)} kcal

"""

    # Content inside tabs
    with tab1:
        st.header("🏋️ Workout Plan")

        if goal_type == "Lose weight":
            workout_plan = """
            **Weekly Plan:**
            - 30 minutes brisk walking 5x a week
            - 2x Strength training sessions (full body circuits)
            - 1x HIIT cardio session (20 mins)
            """
        elif goal_type == "Gain muscle":
            workout_plan = """
            **Weekly Plan:**
            - 4x Strength training (Push/Pull/Legs/Upper Split)
            - 1x Conditioning session (rowing, sled pushes)
            """
        else:
            workout_plan = """
            **Weekly Plan:**
            - 3x Full-body strength workouts
            - 2x Cardio sessions (light jog, swimming, cycling)
            """

        st.markdown(workout_plan)
        plan_text += workout_plan.replace("**", "").replace("-", "*") + "\n"

    with tab2:
        st.header("🥗 Nutrition Plan")

        nutrition_plan = """
        **Focus on:**
        - High-protein meals
        - Plenty of vegetables and whole grains
        - Healthy fats like avocado, nuts, and olive oil
        - Stay hydrated

        **Sample Easy Recipes:**

        🥤 **Protein Smoothie:**
        - 1 scoop protein powder
        - 1 banana
        - 1 tbsp peanut butter
        - 1 cup almond milk

        🍽️ **Chicken Power Bowl:**
        - Grilled chicken breast
        - Quinoa or brown rice
        - Roasted veggies
        - Olive oil drizzle

        🍳 **Veggie Omelette:**
        - 2 eggs
        - Spinach, tomatoes, mushrooms
        - Sprinkle of cheese
        """
        st.markdown(nutrition_plan)
        plan_text += nutrition_plan.replace("**", "").replace("-", "*") + "\n"

    # Provide download button
    st.subheader("📥 Download Your Custom Plan:")
    st.download_button(label="Download My Plan",
                       data=plan_text,
                       file_name="fitness_goal_plan.txt",
                       mime="text/plain")
