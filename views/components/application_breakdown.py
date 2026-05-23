

import streamlit as st


# =========================
# APPLICATION BREAKDOWN COMPONENT
# =========================
def render_application_breakdown(df):

    st.header("Application Breakdown")
    st.caption(
        "Review the current structure of your application pipeline by status and work arrangement."
    )

    status_col, work_col = st.columns(2)

    with status_col:
        st.subheader("Status Breakdown")

        status_counts = df["Status"].value_counts().reset_index()
        status_counts.columns = ["Status", "Applications"]

        st.dataframe(
            status_counts,
            width="stretch",
            hide_index=True
        )

    with work_col:
        st.subheader("Work Arrangement")

        work_arrangement_counts = (
            df["Work Arrangement"]
            .fillna("Not Specified")
            .replace("", "Not Specified")
            .value_counts()
            .reset_index()
        )

        work_arrangement_counts.columns = [
            "Work Arrangement",
            "Applications"
        ]

        st.dataframe(
            work_arrangement_counts,
            width="stretch",
            hide_index=True
        )