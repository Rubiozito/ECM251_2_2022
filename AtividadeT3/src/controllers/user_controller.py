import streamlit as st
from models.user import User

class UserController():
    def __init__(self):
        if "user" not in st.session_state:
            st.session_state.user = None

    