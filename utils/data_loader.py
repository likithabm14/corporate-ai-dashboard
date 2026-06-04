import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file):

    try:
        df = pd.read_csv(file)

        df.drop_duplicates(inplace=True)

        return df

    except Exception as e:
        st.error(f"Error Loading Dataset: {e}")
        return pd.DataFrame()
