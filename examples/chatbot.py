import streamlit as st 
import openai
from streamlit_chat import message
import requests

openai.api_key="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"

def generate_output(prompt):


  res=openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=512
  )
  return res.choices[0].text

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

add_bg_from_url()

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","", key="input")
    return input_text 


user_input = get_text()

if user_input:
    output=generate_output(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
