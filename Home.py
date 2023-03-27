import streamlit as st
import requests
from multiapp import MultiApp
from PIL import Image
from apps import Frequency_VS_Monetary, Introduction, Frequency_VS_Recency,Recency_VS_Monetary# import your app modules here
st.set_page_config(page_title="Snowflake Usage App", layout='wide')
col1, col2= st.columns((1,2))
with col1:
    st.image('H.jpg', width=300)
with col2:
    st.write(
        """
        ## Welcome to the Customer Segmentation Application 👋
        """
        )

    st.markdown(
         """
        Customer Segmentation example with Snowpark using K-Means. Data is queried live from Snowflake
        Sample cluster data that shows the recency, frequency and monetary attributes of each customer

        ### Get started!

        Please select a option :arrow_down_small:
            """
        )

app = MultiApp()   




# Add all your application here
app.add_app("INTRODUCTION", Introduction.app)
app.add_app("FREQUENCY_VS_RECENCY", Frequency_VS_Recency.app)
app.add_app("FREQUENCY_VS_MONETARY", Frequency_VS_Monetary.app)
app.add_app("RECENCY_VS_MONETARY", Recency_VS_Monetary.app)




# The main app
app.run()



