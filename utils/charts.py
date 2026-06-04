import plotly.express as px
import plotly.graph_objects as go


def industry_adoption_chart(df):
    industry = (
        df.groupby("industry")["ai_adoption_level"]
        .mean()
        .reset_index()
        .sort_values(
            by="ai_adoption_level",
            ascending=False
        )
    )

    fig = px.bar(
        industry,
        x="industry",
        y="ai_adoption_level",
        color="ai_adoption_level",
        title="AI Adoption by Industry"
    )

    return fig


def country_revenue_chart(df):
    country = (
        df.groupby("country")["revenue_impact"]
        .sum()
        .reset_index()
    )

    fig = px.choropleth(
        country,
        locations="country",
        locationmode="country names",
        color="revenue_impact",
        title="Revenue Impact by Country"
    )

    return fig


def investment_vs_revenue(df):
    fig = px.scatter(
        df,
        x="ai_investment_usd",
        y="revenue_impact",
        color="industry",
        hover_data=["country"],
        title="AI Investment vs Revenue Impact"
    )

    return fig


def yearly_trend(df):
    trend = (
        df.groupby("year")["ai_adoption_level"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        trend,
        x="year",
        y="ai_adoption_level",
        markers=True,
        title="Yearly AI Adoption Trend"
    )

    return fig


def company_size_distribution(df):
    fig = px.pie(
        df,
        names="company_size",
        title="Company Size Distribution"
    )

    return fig


def ai_maturity_chart(df):
    maturity = (
        df.groupby("ai_maturity_level")
        .size()
        .reset_index(name="count")
    )

    fig = px.bar(
        maturity,
        x="ai_maturity_level",
        y="count",
        color="count",
        title="AI Maturity Levels"
    )

    return fig


def correlation_heatmap(df):
    corr = (
        df.select_dtypes(include="number")
        .corr()
    )

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap"
    )

    return fig
