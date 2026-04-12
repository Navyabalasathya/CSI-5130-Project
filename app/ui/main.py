import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from app.pipeline.self_correcting_pipeline import ask_with_self_correction

st.set_page_config(page_title="NL to SQL AI Assistant", layout="wide")

# GLOBAL STYLES
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
}
h1, h2, h3, h4, h5, h6 {
    color: #e0f7ff !important;
}

/*  Main container (center content) */
.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 2rem;
}

/* Title */
[data-testid="stMarkdownContainer"] h1 {
    color: #00eaff;
    text-align: center;
    font-weight: 1000;
    font-size: 4rem !important;
    letter-spacing: 1px;
    text-shadow: 0 0 10px #00eaff, 0 0 20px #00eaff;
    margin-bottom: 0.2em;
}

/* Subtitle */
[data-testid="stCaptionContainer"] {
    text-align: center;
    color: #e0f7ff;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

/* Input Box */
[data-testid="stTextInput"] input {
    background: rgba(0, 0, 0, 0.5) !important;
    color: #ffffff !important;
    caret-color: #ffffff;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #00eaff, #38bdf8);
    color: black;
    border-radius: 12px;
    font-weight: bold;
    padding: 12px;
    margin-top: 10px;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 15px rgba(0,234,255,0.6);
}

/* Results Card */
.result-card {
    background: rgba(255,255,255,0.06);
    padding: 16px;
    border-radius: 14px;
    margin-top: 20px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Explanation Box */
.explanation-box {
    background: rgba(0, 234, 255, 0.08);
    padding: 18px;
    border-radius: 14px;
    margin-top: 10px;
    border: 1px solid rgba(0, 234, 255, 0.2);
    box-shadow: 0 0 20px rgba(0, 234, 255, 0.1);
    color: #e0f7ff;
    line-height: 1.6;
}

/* Section Headers */
h3 {
    color: #00eaff !important;
    font-weight: 600;
    margin-top: 1.5rem;
    text-shadow: 0 0 8px rgba(0, 234, 255, 0.6);
}

/* Spinner text */
[data-testid="stSpinner"] {
    color: #e0f7ff !important;
    font-size: 18px;
    text-align: center;
}

/* Spinner animation color */
[data-testid="stSpinner"] svg {
    stroke: #00eaff !important;
}

/* Expander header */
[data-testid="stExpander"] summary {
    color: #e0f7ff !important;
    font-size: 16px;
    font-weight: 600;
}

/* Expander content */
[data-testid="stExpander"] div {
    color: #ffffff !important;
}

</style>
""", unsafe_allow_html=True)

# HEADER
st.title("DataInsights")
st.caption("AI-powered Natural language to SQL assistant — turn questions into insights instantly.")

# INPUT
question = st.text_input("", placeholder="💬 Ask your question here...")

# ACTION
if st.button("Get Insights"):
    if question:

        with st.spinner("Searching..."):
            results, explanation, context = ask_with_self_correction(question)

        # RESULTS
        st.markdown("### Query Results")
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.write(results)
        st.markdown('</div>', unsafe_allow_html=True)

        #  EXPLANATION
        st.markdown("### Explanation")
        st.markdown(f'<div class="explanation-box">{explanation}</div>', unsafe_allow_html=True)

        # CONTEXT
        with st.expander("Retrieved Context (RAG)"):
            st.write(context)

    else:
        st.warning("Please enter a question.")