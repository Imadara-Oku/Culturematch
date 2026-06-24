import streamlit as st
from core.session import load_master_data
import pandas as pd
import os


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def show():
    st.title("Company Portal")

    # -----------------------------
    # FILE UPLOAD (SAFE)
    # -----------------------------
    uploaded = st.file_uploader("Upload Company PDF", type="pdf")

    if uploaded:
        os.makedirs("data/uploads", exist_ok=True)

        file_path = f"data/uploads/company_file.pdf"
        with open(file_path, "wb") as f:
            f.write(uploaded.getbuffer())

        st.success("Uploaded successfully")

