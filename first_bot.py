# First
import openai
from PIL import Image
import streamlit as st
from pathlib import Path
import random
import character

image_path = Path('streamlit/images/logo.png')
logo = Image.open(image_path)
st.set_page_config(
    page_title="Innovation Bot",
    page_icon=logo,
)

with st.sidebar:
    image_path = Path('streamlit/images/logo1.png')
    logo = Image.open(image_path)
    st.image(logo)
    st.title("Welcome to Waterstons Innovation bot!")
    st.markdown("This chatbot will answer all of your questions about robot dogs.")
    st.markdown("For more information about our team and what we get up to please check out our **substack:** https://waterstonsinnovation.substack.com/")

image_path = Path('streamlit/images/robot_dog.png')
image1 = Image.open(image_path)
st.image(image1, use_column_width=True)


image_path = Path('streamlit/images/assistant.png')
assistant_img = Image.open(image_path)
image_path = Path('streamlit/images/user.png')
user_img = Image.open(image_path)

if "characters" not in st.session_state:
    st.session_state["characters"] = [
        Character(name = "Andrew", description = "Andrew smells real good. He talks about it a lot though. Like a weird amount.")
    ]

st.title("") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "user", "content": "What is the capital of England?"},
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
#st.chat_message("assistant", avatar=assistant_img).write("Can I interest you in a robot dog?")

if prompt := st.chat_input():
    openai.api_key = st.secrets.api_credentials.api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar=user_img).write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant", avatar=assistant_img).write(msg.content)

