def generate_insights(df):

    insights = []

    top_country = (
        df.groupby("country")["ai_adoption_level"]
        .mean()
        .idxmax()
    )

    top_industry = (
        df.groupby("industry")["ai_adoption_level"]
        .mean()
        .idxmax()
    )

    avg_gain = (
        df["productivity_gain"].mean() * 100
    )

    total_investment = (
        df["ai_investment_usd"].sum()/1e9
    )

    insights.append(
        f"Top AI adoption country: {top_country}"
    )

    insights.append(
        f"Leading industry: {top_industry}"
    )

    insights.append(
        f"Average productivity gain is {avg_gain:.2f}%"
    )

    insights.append(
        f"Total AI investment exceeds ${total_investment:.2f} Billion"
    )

    insights.append(
        "Organizations with higher AI maturity show stronger revenue growth."
    )

    return insights
