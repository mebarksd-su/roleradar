import streamlit as st


def render_dashboard_metrics(
    total_applications,
    applied_count,
    interview_count,
    offer_count,
    conversion_rate
):

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Total Applications",
        total_applications
    )

    col2.metric(
        "Applied",
        applied_count
    )

    col3.metric(
        "Interviews",
        interview_count
    )

    col4.metric(
        "Offers",
        offer_count
    )

    col5.metric(
        "Interview Rate",
        f"{conversion_rate}%"
    )