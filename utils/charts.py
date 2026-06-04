import plotly.express as px

def adoption_trend_chart(df):

    if "year" not in df.columns:
        return px.line(title="Year column not found")

    trend = (
        df.groupby("year")
        .size()
        .reset_index(name="count")
    )

    fig = px.line(
        trend,
        x="year",
        y="count",
        title="AI Adoption Trend"
    )

    return fig


def industry_chart(df):

    if "industry" not in df.columns:
        return px.bar(title="Industry column not found")

    industry = (
        df["industry"]
        .value_counts()
        .reset_index()
    )

    industry.columns = ["industry", "count"]

    fig = px.bar(
        industry,
        x="industry",
        y="count",
        title="Industry Distribution"
    )

    return fig


def country_chart(df):

    if "country" not in df.columns:
        return px.bar(title="Country column not found")

    country = (
        df["country"]
        .value_counts()
        .reset_index()
    )

    country.columns = ["country", "count"]

    fig = px.choropleth(
        country,
        locations="country",
        locationmode="country names",
        color="count",
        title="Country Wise Distribution"
    )

    return fig


def investment_vs_revenue_chart(df):

    required_cols = ["ai_investment_usd", "revenue_impact"]

    if not all(col in df.columns for col in required_cols):
        return px.scatter(title="Required columns not found")

    fig = px.scatter(
        df,
        x="ai_investment_usd",
        y="revenue_impact",
        title="Investment vs Revenue Impact"
    )

    return fig
