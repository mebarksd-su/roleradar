

import streamlit as st


# =========================
# RECENT APPLICATIONS COMPONENT
# =========================
def render_recent_applications(df):

    st.header("Recent Applications")

    if len(df) == 0:
        st.info("No recent applications available.")
        return

    recent_df = df.sort_values(
        by="Date Added",
        ascending=False
    ).head(5)

    display_recent_df = recent_df.drop(
        columns=["Application ID"],
        errors="ignore"
    )

    st.dataframe(
        display_recent_df,
        width="stretch",
        hide_index=True
    )