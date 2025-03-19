import pandas as pd            # Library for data manipulation
import seaborn as sns          # Library for statistical plotting
import matplotlib.pyplot as plt  # For creating custom plots
import streamlit as st         # Framework for building interactive web apps

# ================================================================================
#Missing Data & Data Quality Checks
#
# This lecture covers:
# - Data Validation: Checking data types, missing values, and ensuring consistency.
# - Missing Data Handling: Options to drop or impute missing data.
# - Visualization: Using heatmaps and histograms to explore data distribution.
# ================================================================================
st.title("Missing Data & Data Quality Checks")
st.markdown("""
This lecture covers:
- **Data Validation:** Checking data types, missing values, and basic consistency.
- **Missing Data Handling:** Options to drop or impute missing data.
- **Visualization:** Using heatmaps and histograms to understand data distribution.
""")

# ------------------------------------------------------------------------------
# Load the Dataset
# ------------------------------------------------------------------------------
# Read the Titanic dataset from a CSV file.
df = pd.read_csv("titanic.csv")

# ------------------------------------------------------------------------------
# Display Summary Statistics
# ------------------------------------------------------------------------------
# Show key statistical measures like mean, standard deviation, etc.
st.write("**Summary Statistics**")
st.write(df.shape) ## gets us the total amount of data in the df 
st.dataframe(df.describe())

# only grabs numerical columns and then to the left their is a summary stat 
# ------------------------------------------------------------------------------
# Check for Missing Values
# ------------------------------------------------------------------------------
# Display the count of missing values for each column.
st.write("**Number of Missing Values by Column**")
st.dataframe(df.isnull().sum())
#creates a bullion mask over the df 
# true numeric reprensetation of 1 and fasle numeric rep of 0 
# ------------------------------------------------------------------------------
# Visualize Missing Data
# ------------------------------------------------------------------------------
# Create a heatmap to visually indicate where missing values occur.
st.subheader("Heatmap of missing values")
fig, ax= plt.subplots() # adding a blank canvas
sns.heatmap(df.isnull(), cmap ="viridis", cbar = False) #drawing the viz
st.pyplot(fig) # revealing the viz
#yellow is missing values and purple is not
# ================================================================================
# Interactive Missing Data Handling
#
# Users can select a numeric column and choose a method to address missing values.
# Options include:
# - Keeping the data unchanged
# - Dropping rows with missing values
# - Dropping columns if more than 50% of the values are missing
# - Imputing missing values with mean, median, or zero
# ================================================================================

st.subheader("Handle Missing Data")

# Let the user select a numeric column to work with.
column = st.selectbox("Choose a column to fill",
df.select_dtypes(include=['number']).columns)
# Provide options for how to handle missing data.
method = st.radio("Choose a method", [
"Original DF",
"Drop Rows",
"Drop Columns (>50% Missing)",
"Impute Mean",
"Impute Median",
"Impute Zero"
])
# Work on a copy of the DataFrame so the original data remains unchanged.
#Creating a copy of the DataFrame for cleaning the data so the original deosnt change 
df_clean = df.copy()
# Apply the selected method to handle missing data.

if method == "Original DF":
    pass # Keep the data unchanged.
elif method == "Drop Rows":
# Remove all rows that contain any missing values.
    df_clean = df_clean.dropna()
elif method == "Drop Columns (>50% Missing)":
# Drop columns where more than 50% of the values are missing.
    df_clean = df_clean.drop(columns=df_clean.columns[df_clean.isnull().mean() >
0.5])
elif method == "Impute Mean":
# Replace missing values in the selected column with the column's mean.
    df_clean[column] = df_clean[column].fillna(df[column].mean())
elif method == "Impute Median":
# Replace missing values in the selected column with the column's median.
    df_clean[column] = df_clean[column].fillna(df[column].median())
elif method == "Impute Zero":
   
# Replace missing values in the selected column with zero.
    df_clean[column] = df_clean[column].fillna(0)
# ------------------------------------------------------------------------------
col1, col2 = st.columns(2)
# --- Original Data Visualization ---
with col1:
    st.subheader("Original Data Distribution")

# Plot a histogram (with a KDE) for the selected column from the original

# Compare Data Distributions: Original vs. Cleaned

# Create two columns in the Streamlit layout for side-by-side comparison.
col1, col2 = st.columns(2)
    #
# Display side-by-side histograms and statistical summaries for the selected column.
# ------------------------------------------------------------------------------

