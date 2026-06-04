import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path):
    """
    Load dataset and perform basic cleaning.
    """
    df = pd.read_csv(file_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna(0)

    return df


def get_numeric_columns(df):
    return df.select_dtypes(include=['int64', 'float64']).columns.tolist()


def get_categorical_columns(df):
    return df.select_dtypes(include=['object']).columns.tolist()
