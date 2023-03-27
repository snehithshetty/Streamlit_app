import streamlit as st
import plotly.express as px
from snowflake.snowpark.session import Session
from config import snowflake_conn_prop
session = Session.builder.configs(snowflake_conn_prop).create()

@st.cache_data
def get_data():
    df = session.table("RFM_Clusters")
    df_pd = df.to_pandas()
    df_pd["Cluster"] = df_pd["Cluster"].astype(str)
    return df_pd

def app():
      
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

            