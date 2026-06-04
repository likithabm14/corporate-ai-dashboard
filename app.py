import streamlit as st
from utils.data_loader import load_data

st.set_page_config(
    page_title="Corporate AI Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Corporate AI Adoption Analytics Dashboard")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Upload your dataset to begin")
    st.stop()

df = load_data(uploaded_file)

if df.empty:
    st.error("Dataset could not be loaded")
    st.stop()

st.success(f"Dataset Loaded Successfully: {len(df)} rows")
st.dataframe(df.head())
