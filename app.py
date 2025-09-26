import streamlit as st
from dotenv import load_dotenv
from graph.graph import app

load_dotenv()

st.set_page_config(page_title="Agentic RAG", layout="wide")
st.title("Agentic RAG")

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

for message in st.session_state["message_history"]:
    _,_, right = st.columns([2,1,8])
    if message["role"]=="user":
        with right:
            with st.chat_message("user"):
                st.text(message["content"])
    else:
        with st.chat_message("assistant"):
            st.text(message["content"])
# User input
question = st.chat_input("Ask question:")

if question:
    _, _, right = st.columns([2,1,8])
    st.session_state["message_history"].append({"role": "user", "content": question})
    with right:
        with st.chat_message("user"):
            st.text(question)
    intial_state = {"question": question}
    with st.chat_message("assistant"):
        ai_message = st.write_stream(message_chunk.content for message_chunk, metadata in app.stream(intial_state, stream_mode="messages"))
    st.session_state["message_history"].append({"role":"assistant", "content": ai_message})

