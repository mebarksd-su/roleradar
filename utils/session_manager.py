import streamlit as st


# =========================
# RADAR LAB SESSION CLEANUP
# =========================

def clear_radar_lab_state():

    keys_to_clear = [
        "analysis_result",
        "uploaded_resume_text",
        "uploaded_resume_file",
        "job_description",
        "match_results",
        "current_analysis",
        "resume_text",
        "match_job_description",
        "ai_gap_explanation",
        "generated_bullet"
    ]

    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]


# =========================
# FULL APP SESSION CLEANUP
# Use this for logout later.
# =========================

def clear_app_session_state():

    keys_to_clear = [
        "company",
        "role",
        "location",
        "job_link",
        "notes",
        "add_app_expanded",
        "success_message",
        "toast_message",
        "analysis_result",
        "uploaded_resume_text",
        "uploaded_resume_file",
        "job_description",
        "match_results",
        "current_analysis",
        "resume_text",
        "match_job_description",
        "ai_gap_explanation",
        "generated_bullet"
    ]

    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]