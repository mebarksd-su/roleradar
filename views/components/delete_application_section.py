

import streamlit as st

from utils.database import delete_application


# =========================
# DELETE APPLICATION COMPONENT
# =========================
def render_delete_application_section(df):

    st.header("Delete Application")

    if len(df) == 0:
        st.info("No applications available to delete.")
        return

    delete_index = st.selectbox(
        "Select Application to Delete",
        df.index,
        format_func=lambda x: f"{df.loc[x, 'Company']} - {df.loc[x, 'Role']}"
    )

    selected_application_id = int(
        df.loc[
            delete_index,
            "Application ID"
        ]
    )

    delete_button = st.button(
        "Delete Selected Application"
    )

    if delete_button:

        delete_application(selected_application_id)

        st.toast(
            "Application deleted successfully."
        )

        st.rerun()