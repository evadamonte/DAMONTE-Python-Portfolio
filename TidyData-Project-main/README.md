### 🧼 Tidy Data Project – 2008 Olympics Medalists

An end-to-end data wrangling project applying **Hadley Wickham’s tidy data principles** to reshape and clean a messy Olympic medalist dataset for analysis.

---

### 🧠 Project Overview
This project focuses on transforming and analyzing the 2008 Olympic Medalist dataset. The raw data was messy, wide-format, and had several combined variables. Using pandas and NumPy, I applied tidy data methods to make it analysis-ready. The project culminates with several insightful visualizations of medal distributions.

---

### 🧰 Setup & Run Instructions
#### 📦 Requirements
- pandas
- numpy
- matplotlib
- seaborn
- jupyter (if running locally)

#### ▶️ Running the Notebook Locally
```bash
# 1. Clone the project repository
https://github.com/evadamonte/DAMONTE-Python-Portfolio.git

# 2. Navigate to the project folder
cd TidyData-Project-main

# 3. Launch the notebook
jupyter notebook Data_Tidy_Project.ipynb
```

---

### 📁 Dataset Description
- **File:** `olympics_08_medalists.csv`
- **Source:** 2008 Olympic medalist dataset

**Key Cleaning & Transformation Steps:**
- Wide → Long format reshaping using `melt()`
- Splitting columns using `str.split()`
- Cleaning missing values and standardizing string cases
- Exported tidy dataset to `tidy_olympics_2008.csv`

---

### 📊 Visualizations Created
- Top 10 sports by medal count (bar chart)
- Gender-based medal distributions
- Heatmap of medals by sport and gender
- Medal type distribution (Gold/Silver/Bronze)

📸 **Example Output**
![Medal by Sport](https://github.com/evadamonte/DAMONTE-Python-Portfolio/blob/main/TidyData-Project-main/number_of_medals.png)

---

### 🔗 Key Links
- 📁 [Tidy Data GitHub Repository](https://github.com/evadamonte/DAMONTE-Python-Portfolio/tree/main/TidyData-Project-main)
- 📓 [Notebook File](https://github.com/evadamonte/DAMONTE-Python-Portfolio/blob/main/TidyData-Project-main/Data_Tidy_Project.ipynb)
- 📄 [README](https://github.com/evadamonte/DAMONTE-Python-Portfolio/blob/main/TidyData-Project-main/README.md)

---

### 📚 References
- [Tidy Data by Hadley Wickham](https://vita.had.co.nz/papers/tidy-data.pdf)
- [pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Matplotlib Docs](https://matplotlib.org/stable/contents.html)
- [Seaborn Docs](https://seaborn.pydata.org/)

---

### 🧠 Skills Demonstrated
- Data reshaping (wide → long)
- Column parsing and missing value handling
- Visualization using seaborn & matplotlib
- Data tidying for reproducible analysis

---

✅ **Outcome:**
A clean and structured dataset, insightful EDA visuals, and improved ability to explore Olympic performance trends.

---

