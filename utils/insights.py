def generate_insights(df):

    insights = {}

    # Top Industry
    top_industry = (
        df.groupby("industry")
        ["ai_adoption_level"]
        .mean()
        .idxmax()
    )

    insights["Top Industry"] = top_industry

    # Top Country
    top_country = (
        df.groupby("country")
        ["revenue_impact"]
        .sum()
        .idxmax()
    )

    insights["Top Country"] = top_country

    # Highest Revenue Impact
    revenue = (
        df["revenue_impact"]
        .sum()
    )

    insights["Total Revenue Impact"] = round(revenue, 2)

    # Total Investment
    investment = (
        df["ai_investment_usd"]
        .sum()
    )

    insights["Total AI Investment"] = round(investment, 2)

    # Average Adoption
    adoption = (
        df["ai_adoption_level"]
        .mean()
    )

    insights["Average AI Adoption"] = round(adoption, 2)

    return insights


def recommendation_engine(df):

    recommendations = []

    avg_adoption = df["ai_adoption_level"].mean()

    if avg_adoption < 50:
        recommendations.append(
            "Increase AI implementation across departments."
        )

    if df["revenue_impact"].mean() > 0:
        recommendations.append(
            "AI investments are producing positive revenue impact."
        )

    if df["ai_investment_usd"].mean() > 100000:
        recommendations.append(
            "High AI investment trend observed."
        )

    return recommendations
