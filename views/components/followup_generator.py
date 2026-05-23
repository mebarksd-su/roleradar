

import streamlit as st

from config.constants import FOLLOW_UP_TYPES


# =========================
# FOLLOW-UP GENERATOR COMPONENT
# =========================
def render_followup_generator(df):

    st.header("AI Follow-Up Generator")
    st.caption("Generate professional follow-up messages for applications, interviews, and networking opportunities. Copy, personalize, and paste directly into your email or LinkedIn outreach.")

    if len(df) == 0:
        st.info("Add an application before generating a follow-up message.")
        return

    selected_application = st.selectbox(
        "Select Application",
        df.index,
        format_func=lambda x: f"{df.loc[x, 'Company']} - {df.loc[x, 'Role']}",
        key="followup_select"
    )

    followup_type = st.selectbox(
        "Follow-Up Type",
        FOLLOW_UP_TYPES
    )

    generate_followup = st.button(
        "Generate Follow-Up Message"
    )

    if generate_followup:

        selected_company = df.loc[
            selected_application,
            "Company"
        ]

        selected_role = df.loc[
            selected_application,
            "Role"
        ]

        generated_message = ""

        if followup_type == "Post-Application Follow-Up":

            generated_message = f"""
Hello {selected_company} Hiring Team,

I hope you are doing well. I recently applied for the {selected_role} position and wanted to follow up regarding my application status.

I remain very interested in the opportunity and would love the chance to contribute my skills and experience to your team.

Thank you for your time and consideration. I look forward to hearing from you.

Best,
Your Name
"""

        elif followup_type == "Interview Thank You":

            generated_message = f"""
Hello {selected_company} Team,

Thank you again for taking the time to speak with me regarding the {selected_role} opportunity.

I enjoyed learning more about the role and the company, and the conversation further increased my interest in joining your team.

I appreciate your consideration and look forward to hearing about next steps.

Best,
Your Name
"""

        elif followup_type == "Recruiter Networking Message":

            generated_message = f"""
Hello,

I hope you are doing well. My name is [Your Name], and I am very interested in opportunities related to the {selected_role} position at {selected_company}.

I would love to connect and learn more about potential opportunities within your organization.

Thank you for your time, and I hope to stay connected.

Best,
Your Name
"""

        st.subheader("Generated Follow-Up Message")

        st.code(
            generated_message,
            language="markdown"
        )