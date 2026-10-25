import streamlit as st
from langchain_core.messages import HumanMessage
from uuid import uuid4

from langgraph_backend import chatbot

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid4())
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if not st.session_state["message_history"]:
    with st.chat_message("assistant"):
        st.text("Hello! How can I assist you today?")

for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    response = chatbot.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config={"configurable": {"thread_id": st.session_state["thread_id"]}},
    )
    ai_message = response["messages"][-1].content

    st.session_state["message_history"].append({"role": "assistant", "content": ai_message})
    with st.chat_message("assistant"):
        st.text(ai_message)