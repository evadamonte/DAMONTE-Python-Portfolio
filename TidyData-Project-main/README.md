# 🧹 Tidy Data Project - Olympics 2008 Medalists

## 📊 Project Overview
The goal of this project is to apply **tidy data principles** to clean, reshape, and analyze a dataset of 2008 Olympic medalists. 

### What is Tidy Data?
According to **Hadley Wickham’s Tidy Data principles**:
- Each variable is stored in its own column.
- Each observation forms its own row.
- Each type of observational unit forms its own table.

By following these principles, we ensure the dataset is clean, structured, and ready for analysis or visualization.

---

## 📥 Instructions to Run the Notebook
### Requirements:
Install the following Python libraries:
- pandas
- numpy
- matplotlib
- seaborn
- jupyter (if running locally)
- You can do this by running the following code:
- import pandas as pd
- import numpy as np

### Running the Project:
We are first going to need to open the terminal and download the files. You can do that by following these steps:
bash
Step 1: Download the Tidy Data folder which contains the data set as well as the notebook 
You can also run this git command that clones the repository from GitHub onto your local computer
git clone https://github.com/evadamonte/TidyData-Project.git
bash
Step 2: navigate to the correct folder:
cd TidyData-Project-main

Step 3: Open a jupyter notebook:
jupyter notebook Data_Tidy_Project.ipynb
---

## 🗂 Dataset Description
**Source:** 2008 Olympics Medalists Dataset (provided in CSV format)  
**File:** `olympics_08_medalists.csv`  

### Preprocessing and Cleaning Steps:
- Reshaped from wide to long format using `melt()`
- Separated combined columns using `str.split()`
- Cleaned strings and removed missing values
- Exported cleaned dataset as `tidy_olympics_2008.csv`

---

## 📊 Visualizations Created
- 📈 Bar chart: Top 10 sports by medal count
- 📈 Bar chart: Medal counts by gender
- 📈 Heatmap: Medal counts by gender and sport
- 📈 Medal type distribution chart colored by **gold**, **silver**, and **bronze**

✅ **Visual Examples:**
### Medal Count by Sport Visualization
![Medal by Sport](https://github.com/evadamonte/TidyData-Project/blob/main/medal_by_sport.png)

---

## 🔗 References
- 📖 [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- 📖 [Tidy Data Principles by Hadley Wickham](https://vita.had.co.nz/papers/tidy-data.pdf)
- 📖 [Seaborn Documentation](https://seaborn.pydata.org/)
- 📖 [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

---

## 💾 Output:
- Cleaned dataset: `tidy_olympics_2008.csv`
- Pivot tables
- Multiple visualizations ready for EDA (Exploratory Data Analysis)

---

✅ **Final Note:**  
This project demonstrates strong data wrangling, cleaning, and visualization skills while adhering to **tidy data principles** — making the dataset analysis-ready and reproducible.
