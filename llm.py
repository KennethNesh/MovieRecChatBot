from langchain_ai21 import ChatAI21
from langchain_ai21 import AI21Embeddings
import streamlit as st
llm = ChatAI21(
    ai21_api_key=st.secrets["AI21_API_KEY"],
    model="jamba-next", # or any other supported model
)
embeddings = AI21Embeddings(
    ai21_api_key=st.secrets["AI21_API_KEY"])