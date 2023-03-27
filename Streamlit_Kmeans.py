# streamlit_app.py

import streamlit as st
import snowflake.connector
from snowflake.snowpark.session import Session
import pandas as pd
import numpy as np
import plotly.express as px

# Snowflake connection info is saved in config.py
from config import snowflake_conn_prop

# Initialize connection.
# Uses st.experimental_singleton to only run once.
session = Session.builder.configs(snowflake_conn_prop).create()

# session = Session.builder.configs(st.secrets["snowflake"]).create()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.

st.header('Customer Segmentation example with Snowpark using K-Means. Data is queried live from Snowflake')

st.write('Sample cluster data that shows the recency, frequency and monetary attributes of each customer')

@st.cache_data
def get_data():
    df = session.table("RFM_Clusters")
    df_pd = df.to_pandas()
    df_pd["Cluster"] = df_pd["Cluster"].astype(str)

    return df_pd

def main():

    st.subheader('Frequency vs Recency')

    df_pd = get_data()
    st.dataframe(df_pd)

    fig = px.scatter(
        df_pd,
        x="FREQUENCY",
        y="RECENCY",
        color="Cluster",
        opacity=0.5
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    st.subheader('Frequency vs Monetary')

    fig = px.scatter(
        df_pd,
        x="FREQUENCY",
        y="MONETARY",
        color="Cluster",
        opacity=0.5
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    st.subheader('Recency vs Monetary')

    fig = px.scatter(
        df_pd,
        x="RECENCY",
        y="MONETARY",
        color="Cluster",
        opacity=0.5
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    st.markdown("**:red[Cluster 2]** are your Loyalists. They generally spend more money and more frequently.")
    st.markdown("**:blue[Cluster 1]** spend less money and less frequently, but they spent in the last 5 months.")
    st.markdown("**:orange[Cluster 3]** spend less money and less frequently, but they spent beyond the last 5 months.")
    st.markdown("**Cluster** **0** sit somewhere in between.")


     if __name__ == "__main__":
        main()