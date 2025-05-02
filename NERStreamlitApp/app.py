import streamlit as st
import spacy
from spacy import displacy
from io import StringIO

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Page configuration
st.set_page_config(page_title="Custom NER App", layout="centered")

# App title
st.title("🧠 Named Entity Recognition (NER) App")
st.write("Explore built-in and custom named entity recognition using spaCy + Streamlit.")

# Text input or file upload
text_input = ""
upload_option = st.radio("📄 Choose how to provide text:", ["Paste text", "Upload .txt file"])

if upload_option == "Paste text":
    text_input = st.text_area("Enter your text below:", height=200)
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
    if uploaded_file:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        text_input = stringio.read()

# Divider
st.markdown("---")

# Add Custom Entity Patterns
st.subheader("🏷️ Add a Custom Entity Rule")

label = st.text_input("Enter entity label (e.g., FOOD, EVENT)").strip()
pattern = st.text_input("Enter one or more patterns (comma-separated)").strip()

if st.button("➕ Add Pattern"):
    if label and pattern:
        # Create or get existing EntityRuler
        if "entity_ruler" in nlp.pipe_names:
            ruler = nlp.get_pipe("entity_ruler")
        else:
            ruler = nlp.add_pipe("entity_ruler", before="ner")

        # Build pattern(s)
        patterns = [p.strip() for p in pattern.split(",")]
        formatted_patterns = [
            {"label": label.upper(), "pattern": [{"LOWER": token.lower()} for token in p.split()]}
            for p in patterns
        ]

        ruler.add_patterns(formatted_patterns)
        st.success(f"✅ Added {len(formatted_patterns)} pattern(s) to label '{label.upper()}'")

# Divider
st.markdown("---")

# Analyze and display entities
if st.button("🚀 Analyze Text"):
    if text_input:
        doc = nlp(text_input)

        # Define custom colors
        colors = {
            "PERSON": "#ADD8E6",    # Light Blue
            "ORG": "#FFD700",       # Gold
            "GPE": "#90EE90",       # Light Green
            "DATE": "#FFA07A",      # Salmon
            "FOOD": "#FF69B4",      # Hot Pink
            "EVENT": "#BA55D3",     # Purple
        }

        options = {"ents": list(colors.keys()), "colors": colors}
        html = displacy.render(doc, style="ent", options=options)
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter or upload text to analyze.")
