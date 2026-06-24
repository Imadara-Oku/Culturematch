import streamlit as st
import pandas as pd


def init_session():
    if "student_profile" not in st.session_state:
        st.session_state.student_profile = None

    if "selected_skills" not in st.session_state:
        st.session_state.selected_skills = []

    if "skill_levels" not in st.session_state:
        st.session_state.skill_levels = {}

    if "profile_draft" not in st.session_state:
        st.session_state.profile_draft = {}

    if "show_remaining_jobs" not in st.session_state:
        st.session_state.show_remaining_jobs = False

    if "company_name" not in st.session_state:
        st.session_state.company_name = None

    if "company_jobs" not in st.session_state:
        st.session_state.company_jobs = []

    if "context" not in st.session_state:
        st.session_state.context = []


def load_master_data():
    return {
        "skills": [
            "Python", "C++", "Embedded C", "VHDL", "Verilog", "FPGA", "IoT",
            "RTOS", "ARM", "Digital Design", "Machine Learning", "Deep Learning",
            "Networking", "React", "Docker", "Linux", "Kubernetes", "AWS", "Azure"
        ],
        "culture": [
            "Fast-paced", "Startup vibe", "Research-heavy", "Corporate structured",
            "Collaborative", "Remote-first", "Office-centric", "Agile sprints"
        ],
        "personality": [
            "Independent", "Team-oriented", "Detail-focused", "Big-picture thinker",
            "Quick learner", "Patient & methodical", "Innovative risk-taker"
        ],
        "character": [
            "Creative", "Disciplined", "Adaptable", "Reliable", "Proactive",
            "Empathetic", "Resilient"
        ],
        "degrees": [
            "B.Eng Computer Engineering",
            "B.Eng Electrical/Electronics Engineering",
            "B.Sc Computer Science",
            "B.Eng Software Engineering",
            "B.Tech Information Technology",
            "Other (please specify)"
        ]
    }
