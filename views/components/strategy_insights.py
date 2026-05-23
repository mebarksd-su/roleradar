

import streamlit as st


# =========================
# STRATEGY INSIGHTS COMPONENT
# =========================
def render_strategy_insights(
    total_applications,
    interview_count,
    offer_count,
    rejected_count,
    conversion_rate
):

    st.header("Application Strategy Insights")

    insights = []

    if total_applications < 10:
        insights.append(
            "Your application volume is still relatively low. Expanding your application reach may increase interview opportunities."
        )

    if conversion_rate >= 20:
        insights.append(
            "Your interview conversion rate is strong. Your resume and targeting strategy appear effective."
        )

    elif conversion_rate >= 10:
        insights.append(
            "Your interview rate is moderate. Small resume optimizations or more targeted applications could improve results."
        )

    else:
        insights.append(
            "Your interview conversion rate is currently low. Consider improving resume tailoring and targeting more aligned positions."
        )

    if rejected_count > interview_count:
        insights.append(
            "You are receiving more rejections than interviews. Focus on improving role fit and resume customization."
        )

    if offer_count > 0:
        insights.append(
            "You are successfully progressing through hiring pipelines. Continue refining your interview preparation process."
        )

    for insight in insights:
        st.info(insight)