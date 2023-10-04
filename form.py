# First
import openai
from PIL import Image
import streamlit as st
from pathlib import Path
import random
import character


with st.form("my form"):
    st.write("Form")
    name = st.text_area("Name")
    description = st.text_area("Description")
    temperature = st.slider("Form slider")
    submitted = st.form_submit_button("Submit")
    

    if submitted:
        st.write("Name", name, "description", description)
    #    #name, description, temperature, starting feeling

