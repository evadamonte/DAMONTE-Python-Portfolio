### 🧠 Custom Named Entity Recognition (NER) App

A web-based NLP app built with **spaCy** and **Streamlit** for visualizing named entities — including support for custom entity types and interactive text uploads.

---

### 🧠 Project Overview
This project lets users explore Named Entity Recognition using spaCy’s built-in models and their own custom labels. Users can paste or upload text, define new entity types (like `EVENT`, `BRAND`, or `FOOD`), and visualize results instantly. Built to support experimentation with user-generated entity rules.

---

### 🧰 Setup & Run Instructions
#### 📦 Requirements
- Python 3.10+
- streamlit
- spacy
- pandas
- Pillow

#### ▶️ Run Locally
```bash
# Clone repository
https://github.com/evadamonte/DAMONTE-Python-Portfolio.git

# Navigate to the app folder
cd NERStreamlitApp

# Run the app
streamlit run app.py
```

---

### 📄 App Features
- 📝 Upload `.txt` files or paste custom text blocks
- 🏷️ Add your own entity rules with `EntityRuler`
- 🎨 View color-coded named entities using spaCy’s DisplaCy visualizer
- 🌚 Dark theme and emojis for improved UX
- ☁️ Live deployment via Streamlit Cloud

---

### 📸 Visual Output Example
![NER Example](images/ner-example.png)

Example sentence:  
_"Taylor Swift performed at **Madison Square Garden** (ORG) in **New York** (GPE) on **August 9, 2023** (DATE)."_

---

### 🔗 Key Links
- 🌐 [Live App](https://damonte-python-portfolio-r2fnqpbevnnb7okbc6hwdf.streamlit.app/)  
- 📁 [GitHub Repository](https://github.com/evadamonte/DAMONTE-Python-Portfolio/tree/main/NERStreamlitApp)

---

### 📚 References
- [spaCy Documentation](https://spacy.io/usage)
- [EntityRuler Guide](https://spacy.io/usage/rule-based-matching#entityruler)
- [Streamlit + spaCy Blog](https://blog.streamlit.io/streamlit-with-spacy/)
- [DisplaCy Visualizer](https://spacy.io/usage/visualizers)

---

### 🧠 Skills Demonstrated
- Natural Language Processing (NLP)
- Rule-based pattern matching
- Interactive UI/UX design
- Streamlit deployment & GitHub collaboration

---

✅ **Outcome:**
A fully functional NER app with both default and custom entity recognition, deployed on the web with clean visuals and user-friendly controls.

---

