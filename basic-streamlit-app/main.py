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

st.button('Hit me')
st.radio('Pick one:', ['female','male'])
st.slider('Slide me', min_value=0, max_value=10)