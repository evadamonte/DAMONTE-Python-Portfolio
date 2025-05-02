import streamlit as st
from PIL import Image

# --- Set page configuration ---
st.set_page_config(page_title="Fitness Goal Tracker", page_icon="💪", layout="centered")

# --- Sidebar image (user photo) ---
try:
    image = Image.open("my_photo.jpg")
    rotated_image = image.rotate(-90, expand=True)
    st.sidebar.image(rotated_image, use_column_width=True)
except:
    st.sidebar.warning("Personal image not found. Using app default visuals.")

# --- App Title and Intro ---
st.title("💪 Fitness Goal Tracker")
st.markdown("<h4 style='color: #4CAF50;'>Plan smarter. Train better. Eat cleaner.</h4>", unsafe_allow_html=True)
st.write("Enter your information below to receive a personalized fitness and nutrition plan tailored to your goals.")

# --- User Input Section ---
st.markdown("### 📋 Your Info:")
weight = st.number_input("Current weight (lbs):", min_value=50, max_value=500)
goal_weight = st.number_input("Goal weight (lbs):", min_value=50, max_value=500)

# Height input: combine feet + inches into total inches
height_feet = st.number_input("Height (feet):", min_value=3, max_value=8)
height_inches = st.number_input("Additional height (inches):", min_value=0, max_value=11)
height = height_feet * 12 + height_inches

age = st.number_input("Age:", min_value=10, max_value=100)
activity_level = st.selectbox("Activity level:", ["Sedentary", "Lightly Active", "Active", "Very Active"])
goal_type = st.selectbox("What is your goal?", ["Lose weight", "Maintain", "Gain muscle"])
location_type = st.selectbox("Preferred workout location:", ["At Home", "Outdoor", "Gym"])

# --- Create Interface Tabs ---
workout_tab, nutrition_tab, motivation_tab, music_tab = st.tabs([
    "🏋️ Workout Plan", "🥗 Nutrition Plan", "🎤 Motivation", "🎵 Workout Music"])

# --- Motivation Tab ---
with motivation_tab:
    st.header("🔥 Motivational Speeches")
    st.write("Need a boost? These short speeches will get your mindset right.")
    st.markdown("**1. Eric Thomas – 'How Bad Do You Want It?'**")
    st.video("https://www.youtube.com/watch?v=lsSC2vx7zFQ")
    st.markdown("**2. Jocko Willink – 'GOOD'**")
    st.video("https://www.youtube.com/watch?v=IdTMDpizis8")
    st.markdown("**3. Les Brown – 'You Gotta Be Hungry'**")
    st.video("https://www.youtube.com/watch?v=KxGRhd_iWuE")

# --- Music Tab ---
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

# --- Plan Generation Logic ---
if st.button("Generate My Plan"):
    # Basic error handling for missing inputs
    if weight == 0 or goal_weight == 0 or height == 0 or age == 0:
        st.error("🚫 Please make sure all input fields are filled out correctly before generating your plan.")
    else:
        # --- Health Calculations ---
        bmi = (weight / (height * height)) * 703

        # BMR calculation using Mifflin-St Jeor equation
        bmr = 10 * (weight * 0.45) + 6.25 * (height * 2.54) - 5 * age + 5
        multiplier = {"Sedentary": 1.2, "Lightly Active": 1.375, "Active": 1.55, "Very Active": 1.725}
        maintenance_calories = bmr * multiplier[activity_level]

        # Adjust calories based on user goal
        goal_calories = maintenance_calories + (-500 if goal_type == "Lose weight" else 300 if goal_type == "Gain muscle" else 0)

        # --- Show Key Metrics ---
        st.subheader("📊 Summary Metrics")
        st.metric(label="Body Mass Index (BMI)", value=f"{bmi:.1f}")
        st.metric(label="Target Daily Calories", value=f"{int(goal_calories)} kcal")

        # --- Personalized BMI Feedback ---
        if bmi < 18.5:
            bmi_status = "Underweight"
            st.success("✅ You're underweight — your plan focuses on strength and high-quality calories.")
        elif bmi < 24.9:
            bmi_status = "Healthy Weight"
            st.success("🟢 You're at a healthy weight — let's maintain and build lean muscle.")
        elif bmi < 29.9:
            bmi_status = "Overweight"
            st.warning("🟠 You're overweight — we'll work on trimming fat and boosting energy.")
        else:
            bmi_status = "Obese"
            st.error("🔴 You're in the obese range — safety and sustainability come first in this plan.")

        # --- Initialize downloadable text ---
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

        # --- Workout Plan Tab Content ---
        with workout_tab:
            st.header("🏋️ Your Personalized Weekly Workout Plan")
            st.markdown("[Click here for YouTube workout demos](https://www.youtube.com/@bodyproject/videos)")

            if bmi_status in ["Overweight", "Obese"]:
                plan = "- 4x Low-impact cardio (march in place, step-ups)\n- 3x Strength (bodyweight squats, wall pushups)\n- Daily stretching & mobility"
            elif bmi_status == "Underweight":
                plan = "- 4x Strength (push-ups, lunges, backpack rows)\n- 2x Yoga or pilates\n- High-calorie post-workout snacks"
            else:
                plan = "- 3x Full-body HIIT (squats, pushups, jumping jacks)\n- 2x Mobility days\n- Optional: resistance band circuits"

            st.markdown(plan)
            plan_text += "\nWorkout Plan:\n" + plan.replace("-", "*")

        # --- Nutrition Tab Content ---
        with nutrition_tab:
            st.header("🥗 Your Nutrition Guide")
            st.markdown("[📽️ Healthy Meal Prep Video](https://www.youtube.com/watch?v=H7zL2ZGqxYo)")
            st.caption("These links and examples will help you build sustainable, nutrient-rich meals.")

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

        # --- Download Final Plan ---
        st.subheader("📥 Download Your Custom Plan:")
        st.download_button("Download My Plan", plan_text, "fitness_plan.txt", "text/plain")
