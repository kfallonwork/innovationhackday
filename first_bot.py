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
    message = f"{output['name']} : {output['utterance']} ({output['thoughts']}) *{output['action']}*"
    st.session_state["messages"].append({"role": output["name"], "content": message})

def addSceneDirection(direction):
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
    st.title("Welcome to Waterstons Friends chat!")
    st.markdown("Reanact our AI generated friends script with us, and add new characters as we go along.")
    st.markdown("For more information about our team and what we get up to please check out our **substack:** https://waterstonsinnovation.substack.com/")
    with st.form("Add a new character"):
        st.write("Form")
        name = st.text_area("Name")
        description = st.text_area("Description")
        action = st.text_area("Action")
        temperature = st.slider("Temperature", min_value=0, max_value=10)
        feeling = st.selectbox(
        'Which feeling does your character have?',
        ('Happy','Sad','Angry')
        )
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Name", name, "description", description, "temperature", temperature/10, "starting_feeling", feeling, "action", action)
            char = Character(name = name, description = description, temperature= temperature, starting_feeling = feeling, starting_action = action)
            c = st.session_state["conversation"]
            c.addParticipant(char)
            st.session_state["messages"].append({"role": char.name, "content": f"*{char.starting_action}*"})


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
    
    joey = Character(name = "Joey", description = "You are Joey. You are lovable but a bit of a doofus. You are handsome and have a way with the ladies. You like to ask them 'how YOU doin'?'. You're smarter than you let on. You work as an actor. You're on a soap opera. You love sandwiches and home cooked Italian food.You live with Chandler. You know that he and Monica are in love but they do know know that you know.")
    
    ross = Character(name = "Ross", description = "You are Ross. You are a paleontologist. You are very precious about your sandwiches. You work in a museum. You have a little boy called Ben. You are divorced. You are in love with Rachel. You play the keyboard very badly. You live by yourself.")
    
    rachel = Character(name = "Rachel", description = "You are Rachel. You work at Ralph Lauren. You are fashionable. You are the source of an extremely popular haircut in the 90s called 'The Rachel'. You aren't the brightest button in the box. You live with Monica.")
    
    chandler = Character(name = "Chandler", description = "You are Chandler. You work at a big technology company. Nobody else seems to know what your job is. You are extremely sarcastic. You and Monica are in love. Nobody else knows.")
    
    monica = Character(name = "Monica", description = "You are Monica. You are a chef. You are a clean freak. You are always cleaning and you hate mess. You cook well. You are in love with Chandler. As far as you know nobody else knows.")
    
    phoebe = Character(name = "Phoebe", description = "You are Phoebe. You are a spiritualist. You play the guitar in a coffee shop. You are not very good at the guitar but you think you are amazing at it. You are a bit loopy. Everyone really loves you. You have a twin sister called Ursula.")
    
    c.addParticipant(joey)
    c.addParticipant(ross)
    c.addParticipant(rachel)
    c.addParticipant(chandler)
    c.addParticipant(monica)
    c.addParticipant(phoebe)
    
    #c.addParticipant(Character(name = "Andrew", description = "Andrew smells real good. He talks about it a lot though. Like a weird amount."))
    #c.addParticipant(Character(name = "Katie", description = "Katie is really really angry about melons."))
    
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
    if prompt.isnumeric():
        for _ in range(int(prompt)):
            progressConversation()
    else:
        addSceneDirection(prompt)
        progressConversation()

