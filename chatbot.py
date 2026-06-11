import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("chat bot")
st.caption("pakistani math ka teacher")

if "message"  not in st.session_state:
    st.session_state.messages=[
        {
            "role":"system",
            "content":"tum ik pakistani math ke teacher ho.English me baat kro"
        }
    ]
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(messages["role"]):
            st.write(messages["content"])

user_input = st.chat_input("ASK QUESTION ONLY FOR MATH....")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role":"user",
        "content":user_input

    })    

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages

    )
    
    ai_reply =response.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(ai_reply)


    st.session_state.messages.append({

        "role":"assistant",
        "content":ai_reply
    })    