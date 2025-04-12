import streamlit as st
from dataclasses import dataclass

# Page configuration
st.set_page_config(page_title="Smart Task Scheduler", page_icon="🗂", layout="centered")

# Custom CSS for soft floral theme
st.markdown(
    """
    <style>
    body {
        background-color: #ffeded;
        color: black;
    }
    .stButton > button {
        background-color: #b4f8c8;
        color: black;
        border: none;
        border-radius: 10px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #a0eac0;
    }
    .task-card {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

