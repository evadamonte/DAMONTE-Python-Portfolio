# 🧠 Custom Named Entity Recognition (NER) App

Welcome to the **Custom NER App**, a web-based tool built with **spaCy** and **Streamlit** that lets users explore Named Entity Recognition (NER) with their own text and custom rules.

This app is designed for interactive NLP experimentation — you can define your own entity labels (like `CELEBRITY`, `BRAND`, or `EVENT`) and see them instantly highlighted alongside default spaCy NER output.

---

## 🎯 App Overview

**Key Features:**

- 📝 Paste or upload `.txt` files
- 🏷️ Add your own NER rules using `EntityRuler`
- 🔍 Analyze the full text for built-in and custom entities
- 🎨 Clean, dark-mode layout with styled output and emojis

---

## 📷 Screenshot

Here’s an example of the app in action, showing spaCy’s default entity recognition:

## 📷 Screenshot

![NER Example](images/ner-example.png)

> “Taylor Swift performed at **Madison Square Garden** (ORG) in **New York** (GPE) on **August 9, 2023** (DATE).”


> Example sentence:  
> _“Taylor Swift performed at **Madison Square Garden** (ORG) in **New York** (GPE) on **August 9, 2023** (DATE).”_

This shows spaCy’s default detection of people, locations, organizations, and dates — no custom patterns required.

---

## 🛠 How to Use the App

### 🔹 Step 1: Enter or Upload Text

Paste a block of text into the input box  
**OR**  
Upload a `.txt` file.

Example: Taylor Swift performed at Madison Square Garden in New York on August 9, 2023.




---

### 🔹 Step 2: (Optional) Add Custom Entity Patterns

You can add your own labels and match patterns.  
Example:

- Label: `EVENT`  
- Pattern: `Eras Tour`

Click ➕ **Add Pattern**

> You can also add multiple patterns separated by commas.

---

### 🔹 Step 3: Click “Analyze Text”

Click 🚀 **Analyze Text** to see the results.  
Entities will be visually highlighted and labeled, including your custom ones.

---


---

## 🚀 App Features

The Custom NER App is designed to help users explore and apply Named Entity Recognition (NER) in an intuitive and interactive way. Here's what you can do:

### 📄 1. Upload or Enter Text

- Paste your own text directly into the input box  
- Or upload a `.txt` file to analyze larger documents  
- Example input: Taylor Swift performed at Madison Square Garden in New York on August 9, 2023.


---

### 🏷️ 2. Add Custom Entity Patterns

- Define your own entity labels (e.g., `FOOD`, `BRAND`, `EVENT`)
- Add one or more patterns (comma-separated) that you want to tag
- Example:

- **Label**: `EVENT`  
- **Pattern**: `Eras Tour`

- **Label**: `ORG`  
- **Pattern**: `Spotify, Chick-fil-A`

> Custom patterns are matched case-insensitively across tokens, and override spaCy’s default NER when added.

---

### 🎨 3. Visualize Entity Highlights

- Click the **"Analyze Text"** button
- View all detected entities — both default and custom — in color-coded highlights
- Each label has a distinct color (e.g., `PERSON` = blue, `ORG` = gold, `GPE` = green)

> The visualization is powered by spaCy’s [DisplaCy](https://spacy.io/usage/visualizers) engine and rendered directly inside the app.

---


## 💻 Local Installation Instructions

To run the app locally on your machine:

```bash
# Clone the repository
git clone https://github.com/yourusername/NERStreamlitApp.git
cd NERStreamlitApp

# Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Run the app
streamlit run app.py


---

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

---

## 📚 References

Here are some of the key resources used to build and support this application:

- 🔗 [spaCy Documentation](https://spacy.io/usage)  
  Comprehensive guide to spaCy's NLP features and components.

- 🔧 [spaCy EntityRuler](https://spacy.io/usage/rule-based-matching#entityruler)  
  Detailed documentation for creating custom entity patterns using the `EntityRuler`.

- 🎨 [DisplaCy Visualizer](https://spacy.io/usage/visualizers)  
  Used for rendering and highlighting named entities within the app.

- 🖥️ [Streamlit Documentation](https://docs.streamlit.io)  
  Framework used for building the interactive app interface.

- 🧠 [Streamlit + spaCy Integration Example](https://blog.streamlit.io/streamlit-with-spacy/)  
  A helpful reference for combining NER and web-based visualization.

---
