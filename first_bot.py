# First
import openai
from PIL import Image
import streamlit as st
from pathlib import Path
import random
from character import Character
from conversation import Conversation

def progressConversation():
    c = st.session_state["conversation"]
    output = c.converse()
    message = f"{output['name']} : {output['utterance']} ({output['thoughts']})"
    st.chat_message(output['name']).write(message)
    st.session_state["messages"].append({"role": output["name"], "content": message})

def addSceneDirection(direction):
    st.chat_message("user").write(direction)
    st.session_state["messages"].append({"role": "user", "content": direction})
    c = st.session_state["conversation"]
    c.addSceneDirection(direction)

image_path = Path('streamlit/images/friends.png')
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

image_path = Path('streamlit/images/friends.png')
image1 = Image.open(image_path)
st.image(image1, use_column_width=True)


image_path = Path('streamlit/images/assistant.png')
assistant_img = Image.open(image_path)
image_path = Path('streamlit/images/user.png')
user_img = Image.open(image_path)

openai.api_key = st.secrets.api_credentials.api_key
    
if "conversation" not in st.session_state:
    c = Conversation("Argue about the relative qualities of the best fruit.")
    c.addParticipant(Character(name = "Andrew", description = "Andrew smells real good. He talks about it a lot though. Like a weird amount."))
    c.addParticipant(Character(name = "Katie", description = "Katie is really really angry about melons."))
    
    st.session_state["conversation"] = c
    st.session_state["messages"] = []
    
    addSceneDirection("Argue about the relative qualities of the best fruit.")
    
    progressConversation()
    progressConversation()
    progressConversation()
    
st.title("") 

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
if prompt := st.chat_input():
    addSceneDirection(prompt)
    progressConversation()

