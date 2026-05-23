

import streamlit as st
import pandas as pd


# =========================
# APPLICATION ACTIVITY COMPONENT
# =========================
def render_application_activity(df):

    st.header("Application Activity")

    if len(df) == 0:
        st.info("No application activity available yet.")
        return

    activity_df = df.copy()

    activity_df["Date Added"] = pd.to_datetime(
        activity_df["Date Added"],
        errors="coerce"
    )

    activity_summary = (
        activity_df
        .groupby(activity_df["Date Added"].dt.date)
        .size()
        .reset_index(name="Applications")
    )

    activity_summary.columns = [
        "Date",
        "Applications"
    ]

    st.subheader("Applications Added By Day")

    st.dataframe(
        activity_summary.sort_values(
            by="Date",
            ascending=False
        ),
        width="stretch",
        hide_index=True
    )

    st.subheader("Recent Application Activity")

    recent_activity = activity_df.sort_values(
        by="Date Added",
        ascending=False
    ).head(5)

    recent_activity_display = recent_activity.drop(
        columns=["Application ID"],
        errors="ignore"
    )

    st.dataframe(
        recent_activity_display,
        width="stretch",
        hide_index=True
    )