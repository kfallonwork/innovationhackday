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

if "conversation" not in st.session_state:
    c = Conversation("Argue about the relative qualities of the best fruit.")
    c.addParticipant(Character(name = "Andrew", description = "Andrew smells real good. He talks about it a lot though. Like a weird amount."))
    c.addParticipant(Character(name = "Katie", description = "Katie is really really angry about melons."))
    st.session_state["conversation"] = c
    
st.title("") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "user", "content": "What is the capital of England?"},
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    openai.api_key = st.secrets.api_credentials.api_key
    st.chat_message("user", avatar=user_img).write(prompt)
    c = st.session_state["conversation"]
    c.addSceneDirection(prompt)
    (name, utterance, feeling, thoughts) = c.converse()
    st.chat_message(name, avatar=assistant_img).write(f"{utterance} ({thoughts})")

