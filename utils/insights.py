def generate_insights(df):

    insights = []

    if df.empty:
        insights.append("Dataset is empty.")
        return insights

    insights.append(
        f"Total Records: {len(df):,}"
    )

    if "country" in df.columns:
        insights.append(
            f"Countries Covered: {df['country'].nunique()}"
        )

    if "industry" in df.columns:
        insights.append(
            f"Industries Covered: {df['industry'].nunique()}"
        )

    return insights
