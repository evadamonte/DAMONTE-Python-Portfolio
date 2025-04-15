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

# Adding a patern 
if st.button("➕ Add Pattern"):
    if label and pattern:
        # Remove existing EntityRuler if already in pipeline
        if "entity_ruler" in nlp.pipe_names:
            nlp.remove_pipe("entity_ruler")
        
        # Add a new EntityRuler before 'ner'
        ruler = nlp.add_pipe("entity_ruler", before="ner")

        # Support multiple comma-separated patterns
        pattern_list = [p.strip() for p in pattern.split(",")]

        # Build all patterns in proper format
        all_patterns = []
        for p in pattern_list:
            tokenized = [{"LOWER": token.lower()} for token in p.split()]
            all_patterns.append({"label": label.upper(), "pattern": tokenized})

        # Add all patterns
        ruler.add_patterns(all_patterns)
        st.success(f"✅ Added {len(all_patterns)} pattern(s) for label '{label.upper()}'.")



# Analyze the Text
if st.button("🚀 Analyze Text"):
    if text_input:
        doc = nlp(text_input)

        # Custom colors for different entity types
        colors = {
            "PERSON": "#ADD8E6",    # Light Blue
            "ORG": "#FFD700",       # Gold
            "GPE": "#90EE90",       # Light Green
            "DATE": "#FFA07A",      # Light Salmon
            "FOOD": "#FF69B4",      # Hot Pink
            "EVENT": "#BA55D3",     # Purple
        }

        # Pass color options to displacy
        options = {"ents": list(colors.keys()), "colors": colors}

        # Render the entity visualization
        html = displacy.render(doc, style="ent", options=options)

        # Display in Streamlit with raw HTML
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter or upload some text.")
