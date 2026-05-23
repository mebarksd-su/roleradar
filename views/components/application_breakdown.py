

import streamlit as st


# =========================
# APPLICATION BREAKDOWN COMPONENT
# =========================
def render_application_breakdown(df):

    st.header("Application Breakdown")

    breakdown_col1, breakdown_col2 = st.columns(2)

    with breakdown_col1:
        st.subheader("Status Breakdown")

        status_counts = df["Status"].value_counts().reset_index()
        status_counts.columns = ["Status", "Applications"]

        st.table(
            status_counts.style.hide(axis="index")
        )

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

        st.table(
            work_arrangement_counts.style.hide(axis="index")
        )

    with breakdown_col2:
        st.subheader("Most Applied Companies")

        company_counts = (
            df["Company"]
            .value_counts()
            .head(3)
            .reset_index()
        )

        company_counts.columns = [
            "Company",
            "Applications"
        ]

        st.table(
            company_counts.style.hide(axis="index")
        )

        st.subheader("Most Applied Locations")

        location_counts = (
            df["Location"]
            .replace("", "Unknown")
            .fillna("Unknown")
            .value_counts()
            .head(3)
            .reset_index()
        )

        location_counts.columns = [
            "Location",
            "Applications"
        ]

        st.table(
            location_counts.style.hide(axis="index")
        )