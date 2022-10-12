import streamlit as st
from models.user import User

class UserController():
    def __init__(self):
        if 'user' not in st.session_state:
            st.session_state.user = None
        self.users_list = [
            User(name="Jones", email= "jones@email.com", password= "1234"),
            User(name="Peixoto", email= "peixoto@email.com", password= "5678"),
            User(name="Miausculo", email= "miausculo@email.com", password= "gato"),
            User(name="admin", email= "admin@email.com", password= "admin")
        ]

    def login(self, name, password):
        user_try = User(name=name, password = password, email = none)
        for u in self.users_list:
            if u.name == user_try.name and u.password == user_try.password:
                st.session_state.user = user_try
                return True
        return False


        

    