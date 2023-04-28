import streamlit as st 
import openai
from streamlit_chat import message
import requests




st.title("WASTE MANAGEMENT")
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://c0.wallpaperflare.com/preview/828/635/683/pollution-rubbish-waste-environment.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

