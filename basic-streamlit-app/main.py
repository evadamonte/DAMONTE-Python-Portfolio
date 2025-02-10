import pandas as pd 
import streamlit as st
st.title("Penguins Data Frame") 
st.write("This app demonstrates shows data about really cute penguins and their make. It includes specifc species, and length of their flipprs and bill ")

st.subheader("Now, let's look at some data!")
st.markdown('_How Cute are Penguins!_') 
df = pd.read_csv("data/penguins.csv")  # Ensure the "data" folder exists with the CSV file
# Display the imported dataset
st.write("Here's the dataset loaded from a CSV file:")
st.dataframe(df)

st.subheader('Penguins associated to a specifc Island')
# Using a selectbox to allow users to filter data by city
# Students learn how to use widgets in Streamlit for interactivity
island = st.selectbox("Select an Island", df["island"].unique())

# Filtering the DataFrame based on user selection
filtered_df = df[df["island"] == island]

# Display the filtered results
st.write(f"Penguins in {island}: island")
st.dataframe(filtered_df)

st.button('Reset')
st.radio('Pick one:', ['female','male'])


bill_length_range = st.slider(
    "Select Bill Length Range (mm)", 
    min_value=int(df["bill_length_mm"].min()), 
    max_value=int(df["bill_length_mm"].max()), 
    value=(int(df["bill_length_mm"].min()), int(df["bill_length_mm"].max()))
)

# Filter the DataFrame based on user selection
filtered_df = df[(df["island"] == island) & 
                 (df["bill_length_mm"] >= bill_length_range[0]) & 
                 (df["bill_length_mm"] <= bill_length_range[1])]

# Add a button to display the filtered data
if st.button("Show Filtered Data"):
    st.write(f"Penguins on {island} island with bill length in the selected range:")
    st.dataframe(filtered_df)