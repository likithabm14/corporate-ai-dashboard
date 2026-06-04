import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.charts import *
from utils.insights import generate_insights

st.set_page_config(
    page_title="Corporate AI Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Corporate AI Adoption Analytics Dashboard")

df = load_data(
    "data/corporate_ai_adoption_dataset.csv"
)

# SIDEBAR

st.sidebar.header("Filters")

industry = st.sidebar.multiselect(
    "Industry",
    df["industry"].unique(),
    default=df["industry"].unique()
)

country = st.sidebar.multiselect(
    "Country",
    df["country"].unique(),
    default=df["country"].unique()
)

filtered = df[
    (df["industry"].isin(industry))
    &
    (df["country"].isin(country))
]

# KPI

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "AI Adoption Avg",
    round(filtered["ai_adoption_level"].mean(),2)
)

c2.metric(
    "Investment",
    f"${filtered['ai_investment_usd'].sum():,.0f}"
)

c3.metric(
    "Revenue Impact",
    f"${filtered['revenue_impact'].sum():,.0f}"
)

c4.metric(
    "Deployments",
    int(filtered["deployment_count"].sum())
)

st.divider()

# CHARTS

col1,col2 = st.columns(2)

with col1:
    st.plotly_chart(
        adoption_by_industry(filtered),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        country_analysis(filtered),
        use_container_width=True
    )

st.plotly_chart(
    investment_vs_revenue(filtered),
    use_container_width=True
)

# YEAR TREND

trend = filtered.groupby(
    "year"
).agg({
    "ai_adoption_level":"mean",
    "revenue_impact":"sum"
}).reset_index()

fig = px.line(
    trend,
    x="year",
    y="ai_adoption_level",
    markers=True,
    title="AI Adoption Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# CORRELATION

st.subheader("Correlation Matrix")

numeric = filtered.select_dtypes(
    include="number"
)

corr = numeric.corr()

heatmap = px.imshow(
    corr,
    text_auto=True
)

st.plotly_chart(
    heatmap,
    use_container_width=True
)

# INSIGHTS

st.subheader("AI Insights")

insights = generate_insights(filtered)

st.success(
    f"""
    🏆 Best Industry:
    {insights['Best Industry']}

    🌍 Top Revenue Country:
    {insights['Top Revenue Country']}
    """
)

# DATA

st.subheader("Dataset")

st.dataframe(filtered)

csv = filtered.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "ai_report.csv",
    "text/csv"
)
