import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import streamlit as st
from app.pipeline.self_correcting_pipeline import ask_with_self_correction

st.set_page_config(page_title="NL to SQL Agent", layout="wide")

st.title("🤖 NL → SQL AI Assistant")

question = st.text_input("Ask a question about the database:")

if st.button("Run Query"):
    if question:
        st.write("### 🧠 Processing...")
        
        # Call your pipeline
        results, explanation = ask_with_self_correction(question)
        st.write("### 📊 Query Results")
        st.write(results)

        st.write("### 🧠 Explanation")
        st.success(explanation)
    else:
        st.warning("Please enter a question.")