import streamlit as st
import pandas as pd

# Streamlit App configuration
st.set_page_config(
    page_title="Ticker Data",
    layout="wide",
)

# Reading the saved data
data = pd.read_parquet("ticker_data_gzip")


# Selectbox to slect the ticker option
ticker = st.selectbox(
    "Select Ticker",
    data["issuer_code"].unique()
)

st.write("Showing data for ", ticker)

# Showing the data with selected 'ticker'
st.write(data[data["issuer_code"] == ticker])

# Checkbox for showing the tickers with 'Trading Halt'
if st.checkbox("Show tickers with 'Trading Halt'"):
    chart_data = data[data["header"].str.contains("Trading Halt", case=False, na=False)]["issuer_code"]
    st.write(chart_data.reset_index(drop=True))