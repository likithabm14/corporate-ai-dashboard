import plotly.express as px

def adoption_trend_chart(df):

    trend = (
        df.groupby("year")["ai_adoption_level"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        trend,
        x="year",
        y="ai_adoption_level",
        title="AI Adoption Trend"
    )

    return fig


def industry_chart(df):

    industry = (
        df.groupby("industry")["ai_adoption_level"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        industry,
        x="industry",
        y="ai_adoption_level",
        title="Industry-wise AI Adoption"
    )

    return fig


def country_chart(df):

    country = (
        df.groupby("country")["ai_adoption_level"]
        .mean()
        .reset_index()
    )

    fig = px.choropleth(
        country,
        locations="country",
        locationmode="country names",
        color="ai_adoption_level",
        title="Global AI Adoption"
    )

    return fig


def investment_vs_revenue_chart(df):

    fig = px.scatter(
        df.sample(5000),
        x="ai_investment_usd",
        y="revenue_impact",
        color="industry",
        title="Investment vs Revenue Impact"
    )

    return fig
