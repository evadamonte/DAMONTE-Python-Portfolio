import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Custom CSS Styling for Dark Theme Vibes
st.markdown(
    """
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #FF69B4;
            text-align: center;
            padding: 10px 0;
        }
        .subtitle {
            font-size: 20px;
            color: #FFB6C1;
            padding-top: 10px;
        }
        .stTextInput>div>div>input {
            color: #FF69B4;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown('<div class="title">🧠 Custom Named Entity Recognition (NER) App</div>', unsafe_allow_html=True)

# Text Input Section
st.subheader("📝 Enter Text or Upload File")
text_input = st.text_area("✏️ Paste text below or upload a file", height=200)

uploaded_file = st.file_uploader("📁 Upload a .txt file", type=["txt"])
if uploaded_file is not None:
    text_input = uploaded_file.read().decode("utf-8")

# Custom Entity Inputs
st.subheader("🔧 Add a Custom Entity Rule")
label = st.text_input("🏷️ Entity Label (e.g., FOOD, BRAND, CELEBRITY)")
pattern = st.text_input("🔍 Pattern to Match (e.g., Starbucks, Taylor Swift)")

# Apply Custom Entity Pattern
if st.button("➕ Add Pattern"):
    if label and pattern:
        # Reset any existing EntityRuler
        if "entity_ruler" in nlp.pipe_names:
            nlp.remove_pipe("entity_ruler")
        ruler = nlp.add_pipe("entity_ruler", before="ner")
        ruler.add_patterns([{"label": label.upper(), "pattern": pattern}])
        st.success(f"✅ Added pattern '{pattern}' with label '{label.upper()}'")

# Analyze the Text
if st.button("🚀 Analyze Text"):
    if text_input:
        doc = nlp(text_input)
        html = displacy.render(doc, style="ent", jupyter=False)
        # Add inline color styling to entities
        html = html.replace("class=\"entity\"", "class=\"entity\" style=\"background:#FF69B4;padding:5px;border-radius:8px;\"")
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please input or upload text to analyze.")