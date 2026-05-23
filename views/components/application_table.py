

import streamlit as st
import pandas as pd

from utils.data_manager import save_applications


# =========================
# APPLICATION TABLE COMPONENT
# =========================
def render_application_table(df):

    st.header("Application List")

    for index, row in df.iterrows():

        application_col1, application_col2, application_col3, application_col4, application_col5, application_col6, application_col7, application_col8 = st.columns([
            2,
            2,
            1.5,
            1.5,
            1.5,
            2,
            1,
            1
        ])

        with application_col1:
            st.write(row["Company"])

        with application_col2:
            st.write(row["Role"])

        with application_col3:
            st.write(row["Status"])

        with application_col4:
            location_value = (
                row["Location"]
                if pd.notna(row["Location"])
                else "Unknown"
            )

            st.write(location_value)

        with application_col5:
            updated_status = st.selectbox(
                "Update Status",
                options=[
                    "Applied",
                    "Interviewing",
                    "Offer",
                    "Rejected",
                    "Ghosted"
                ],
                index=[
                    "Applied",
                    "Interviewing",
                    "Offer",
                    "Rejected",
                    "Ghosted"
                ].index(row["Status"]),
                key=f"status_{index}",
                label_visibility="collapsed"
            )

        with application_col6:
            updated_notes = st.text_area(
                "Notes",
                value=row.get("Notes", ""),
                key=f"notes_{index}",
                height=80,
                label_visibility="collapsed"
            )

        with application_col7:
            if st.button(
                "Save",
                key=f"save_{index}"
            ):

                df.at[index, "Status"] = updated_status
                df.at[index, "Notes"] = updated_notes

                save_applications(df)

                st.toast(
                    f"Saved notes for {row['Company']}"
                )

                

        with application_col8:
            if st.button(
                "Delete",
                key=f"delete_{index}"
            ):

                updated_df = df.drop(index=index)

                save_applications(updated_df)

                st.toast(
                    f"Deleted {row['Company']} application"
                )

                st.rerun()

        st.divider()