# 🧠 Custom Named Entity Recognition (NER) App

Welcome to the **Custom NER App**, a user-friendly web application built with **spaCy** and **Streamlit**. This app allows users to explore **Named Entity Recognition** by uploading their own text, defining custom entity labels, and instantly visualizing the results.

Whether you're working with news, social media, or custom datasets, this app gives you full control over how entities like names, locations, brands, or any term you define are detected and displayed.

---

## 🎯 App Overview

This application allows users to:

- 📝 Paste or upload their own `.txt` files
- 🏷️ Create custom NER rules using spaCy’s `EntityRuler`
- 🚀 Analyze text with both default and custom entities
- 🎨 View a beautiful **color-coded, dark-themed** output with labeled highlights

It’s built to be intuitive, fast, and educational — no coding required.

---

## 📷 Screenshot

> _“Taylor Swift was seen at **In-N-Out** (ORG) eating a **Double-Double** (FOOD) in **Los Angeles** (GPE).”_

![screenshot](images/ner-example.png)

_Above: Entities are highlighted using spaCy’s NER model + your custom patterns._

---

## ⚙️ How to Use the App

### 🔹 Step 1: Enter or Upload Text

Paste a block of text in the input box  
**OR**  
Upload a `.txt` file.

### 🔹 Step 2: Add a Custom Entity Rule

Fill in the two fields under “🔧 Add a Custom Entity Rule”:

- **Label** → Example: `FOOD`
- **Pattern** → Example: `Double-Double`

Click **"➕ Add Pattern"** to apply it.

---

### 🔹 Step 3: Analyze the Text

Click **"🚀 Analyze Text"** to run spaCy’s NLP pipeline and view the visual output.  
Custom and built-in entities will appear highlighted with their labels.

---

## 💻 Local Installation Instructions

To run the app on your local machine:

1. **Clone this repository**

```bash
git clone https://github.com/yourusername/NERStreamlitApp.git
cd NERStreamlitApp

## Install the required librarys 
pip install -r requirements.txt
python -m spacy download en_core_web_sm

## Run the Streamlit App!!
streamlit run app.py

## 🌐 Live Demo

Want to try the app online without installing anything?

👉 [Click here to launch the app on Streamlit Cloud](https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl)

## 📁 Project Structure

NERStreamlitApp/ ├── app.py # Main Streamlit app ├── requirements.txt # Required Python packages ├── README.md # App documentation ├── .streamlit/ │ └── config.toml # Dark theme and UI settings └── images/ └── ner-example.png # Screenshot of highlighted NER output

## 🧠 Powered By

| Tool          | Description                                 |
|---------------|---------------------------------------------|
| `spaCy`       | NLP model for Named Entity Recognition      |
| `EntityRuler` | Rule-based pattern matching for custom NER  |
| `Streamlit`   | Web interface and interactive dashboard     |
| `DisplaCy`    | Visualization for named entities            |

---

## 📎 Resources

- [spaCy: EntityRuler Docs](https://spacy.io/usage/rule-based-matching#entityruler)
- [Streamlit Documentation](https://docs.streamlit.io)
- [DisplaCy Visualizer](https://spacy.io/usage/visualizers)
