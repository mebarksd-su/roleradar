import streamlit as st

from utils.analytics_queries import (
    get_applications_per_week,
    get_top_locations,
    get_top_companies
)


# =========================
# RADAR INTELLIGENCE COMPONENT
# =========================
def render_radar_intelligence():

    st.subheader("Radar Intelligence")

    st.caption(
        "Track application momentum, hiring concentration, and emerging trends across your job search pipeline."
    )

    intelligence_col1, intelligence_col2 = st.columns(2)

    with intelligence_col1:

        st.subheader("Application Velocity")

        weekly_activity = get_applications_per_week()

        if len(weekly_activity) > 0:

            weekly_activity.columns = [
                "Week",
                "Applications"
            ]

            weekly_activity["Week"] = (
                "Week " + weekly_activity["Week"].astype(str)
            )

            st.caption(
                "Applications submitted across tracked calendar weeks."
            )

            st.dataframe(
                weekly_activity,
                width="stretch",
                hide_index=True
            )

        else:

            st.info(
                "Not enough application history available yet."
            )

        st.subheader("Top Hiring Locations")

        top_locations = get_top_locations()

        if len(top_locations) > 0:

            st.caption(
                "Geographic areas receiving the most application focus."
            )

            st.dataframe(
                top_locations,
                width="stretch",
                hide_index=True
            )

        else:

            st.info(
                "No location intelligence available yet."
            )

    with intelligence_col2:

        st.subheader("Top Targeted Companies")

        top_companies = get_top_companies()

        if len(top_companies) > 0:

            st.caption(
                "Organizations targeted most frequently across your pipeline."
            )

            st.dataframe(
                top_companies,
                width="stretch",
                hide_index=True
            )

        else:

            st.info(
                "No company intelligence available yet."
            )

        st.subheader("System Observations")

        st.success(
            "Analytics metrics are now powered by centralized SQL query intelligence."
        )

        st.caption(
            "Future radar systems will support hiring heatmaps, industry tracking, and advanced pipeline analytics."
        )