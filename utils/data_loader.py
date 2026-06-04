import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/corporate_ai_adoption_dataset.csv")
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()
