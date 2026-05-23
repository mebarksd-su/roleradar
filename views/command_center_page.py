import streamlit as st
import pandas as pd
from datetime import date

from utils.database import insert_application

from utils.job_link_parser import infer_application_details_from_link
from config.constants import (
    APPLICATION_STATUSES,
    FILTER_STATUS_OPTIONS,
    WORK_ARRANGEMENTS,
    APP_TAGLINE
)

from views.components.dashboard_metrics import render_dashboard_metrics
from views.components.followup_generator import render_followup_generator
from views.components.application_breakdown import render_application_breakdown
from views.components.application_activity import render_application_activity
from views.components.recent_applications import render_recent_applications
from views.components.strategy_insights import render_strategy_insights
from views.components.delete_application_section import render_delete_application_section
from views.components.application_table import render_application_table



# =========================
# COMMAND CENTER PAGE
# =========================
def render_command_center_page(df):

    st.title("Command Center")

    st.write(APP_TAGLINE)

    # =========================
    # ADD NEW APPLICATION
    # =========================

    with st.expander(
        "Add New Application",
        expanded=st.session_state.get("add_app_expanded", False)
    ):

        st.header("Add New Application")

        if "company" not in st.session_state:
            st.session_state.company = ""

        if "role" not in st.session_state:
            st.session_state.role = ""

        if "location" not in st.session_state:
            st.session_state.location = ""

        if "job_link" not in st.session_state:
            st.session_state.job_link = ""

        if "notes" not in st.session_state:
            st.session_state.notes = ""

        job_link = st.text_input(
            "Job Link",
            key="job_link"
        )

        auto_fill_button = st.button(
            "Try Auto-Fill from Job Link"
        )

        if auto_fill_button:

            if st.session_state.job_link.strip() == "":
                st.warning(
                    "Paste a job link first, then try auto-fill."
                )

            else:

                inferred_details = infer_application_details_from_link(
                    st.session_state.job_link
                )

                parser_notes = inferred_details.get("notes", [])

                st.session_state.company = ""
                st.session_state.role = ""

                if inferred_details["company"]:
                    st.session_state.company = inferred_details["company"]

                if inferred_details["role"]:
                    st.session_state.role = inferred_details["role"]

                if (
                    inferred_details["company"]
                    or inferred_details["role"]
                ):

                    st.success(
                        "RoleRadar filled what it could. Review the fields below, then click Add Application to save."
                    )

                    for note in parser_notes:
                        st.info(note)

                else:

                    st.info(
                        "RoleRadar could not confidently auto-fill this link yet. Add the details manually."
                    )

                    for note in parser_notes:
                        st.info(note)

        company = st.text_input(
            "Company Name",
            key="company"
        )

        role = st.text_input(
            "Job Title",
            key="role"
        )

        location = st.text_input(
            "Location",
            key="location"
        )

        work_arrangement = st.selectbox(
            "Work Arrangement",
            WORK_ARRANGEMENTS
        )

        status = st.selectbox(
            "Application Status",
            APPLICATION_STATUSES
        )

        notes = st.text_area(
            "Notes",
            key="notes"
        )

        submit_button = st.button(
            "Add Application"
        )

        if submit_button:

            if company.strip() == "" or role.strip() == "":

                st.error(
                    "Company name and job title are required."
                )

            else:

                new_application = {
                    "Date Added": str(date.today()),
                    "Company": company.strip(),
                    "Role": role.strip(),
                    "Location": location.strip(),
                    "Work Arrangement": work_arrangement,
                    "Status": status,
                    "Job Link": job_link.strip(),
                    "Notes": notes.strip()
                }

                insert_application(new_application)

                st.session_state[
                    "success_message"
                ] = "Application saved successfully."

                st.session_state[
                    "add_app_expanded"
                ] = False

                del st.session_state["company"]
                del st.session_state["role"]
                del st.session_state["location"]
                del st.session_state["job_link"]
                del st.session_state["notes"]

                st.rerun()

    # =========================
    # DASHBOARD
    # =========================

    st.header("Dashboard")

    total_applications = len(df)

    applied_count = len(
        df[df["Status"] == "Applied"]
    )

    interview_count = len(
        df[df["Status"] == "Interviewing"]
    )

    offer_count = len(
        df[df["Status"] == "Offer"]
    )

    conversion_rate = 0

    if total_applications > 0:
        conversion_rate = round(
            (
                interview_count
                / total_applications
            ) * 100,
            1
        )

    render_dashboard_metrics(
        total_applications,
        applied_count,
        interview_count,
        offer_count,
        conversion_rate
    )

    st.write(
        f"You have {total_applications} total applications, "
        f"{interview_count} interviews, and {offer_count} offers tracked."
    )

    # =========================
    # APPLICATION BREAKDOWN
    # =========================

    render_application_breakdown(df)

    # =========================
    # EXPORT DATA
    # =========================

    st.header("Export Data")

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Applications CSV",
        data=csv_data,
        file_name="roleradar_applications.csv",
        mime="text/csv"
    )

    # =========================
    # RECENT APPLICATIONS
    # =========================

    render_recent_applications(df)

    # =========================
    # AI FOLLOW-UP GENERATOR
    # =========================

    render_followup_generator(df)

    # =========================
    # APPLICATION ACTIVITY
    # =========================

    render_application_activity(df)

    # =========================
    # APPLICATION STRATEGY INSIGHTS
    # =========================

    rejected_count = len(
        df[df["Status"] == "Rejected"]
    )

    render_strategy_insights(
        total_applications,
        interview_count,
        offer_count,
        rejected_count,
        conversion_rate
    )

    # =========================
    # MANAGE APPLICATIONS
    # =========================

    st.header("Manage Applications")

    st.subheader("Filter Applications")

    search_term = st.text_input(
        "Search Company or Job Title",
        key="manage_search"
    )

    status_filter = st.selectbox(
        "Filter by Status",
        FILTER_STATUS_OPTIONS,
        key="manage_status_filter"
    )

    filtered_df = df.copy()

    if search_term:
        filtered_df = filtered_df[
            filtered_df["Company"].str.contains(
                search_term,
                case=False,
                na=False
            )
            |
            filtered_df["Role"].str.contains(
                search_term,
                case=False,
                na=False
            )
        ]

    if status_filter != "All":
        filtered_df = filtered_df[
            filtered_df["Status"] == status_filter
        ]

    st.write(
        f"Showing {len(filtered_df)} matching applications."
    )

    render_application_table(filtered_df)

    # =========================
    # DELETE APPLICATION
    # =========================

    render_delete_application_section(df)
