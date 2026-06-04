import streamlit as st

from utils.data_loader import load_data
from utils.charts import (
    adoption_trend_chart,
    industry_chart,
    country_chart,
    investment_vs_revenue_chart
)
from utils.insights import generate_insights

st.set_page_config(
    page_title="Corporate AI Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Corporate AI Adoption Dashboard")

df = load_data()

if df.empty:
    st.stop()

st.subheader("Dataset Preview")

st.dataframe(df.head())

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        adoption_trend_chart(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        industry_chart(df),
        use_container_width=True
    )

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        country_chart(df),
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        investment_vs_revenue_chart(df),
        use_container_width=True
    )

st.divider()

st.subheader("Insights")

for insight in generate_insights(df):
    st.success(insight)
