import streamlit as st
from core.llm_engine import build_matcher
import time
import pickle
import os
import core.rag_merger as rag_merger


def show():

    full_start = time.time()

    st.title("AI Match Engine")

    student = st.session_state.get("student_profile")
    print(student)

    if not student:
        st.warning("Create student profile first")
        return

    rag = rag_merger.RAG()

    with st.spinner("Finding your best job matches..."):
        response = rag(student_profile=str(student))

    st.session_state["company_jobs"] = response.ranked_fits
    output = sorted(response.ranked_fits,
                    key=lambda x: x.fit_score, reverse=True)[:5]

    for idx, fit in enumerate(output):
        st.markdown("---")
        st.write(f"Job Match {idx + 1}")
        st.subheader(f"Job Title: {fit.job_title}")
        st.metric("Fit Score", fit.fit_score)
        st.write(fit.reasoning)

    full_end = time.time()
    print(f"Total match engine time: {full_end - full_start} seconds")
