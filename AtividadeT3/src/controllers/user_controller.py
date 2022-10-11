import streamlit as st
from models.user import User

class UserController():
    def __init__(self):
        if "user" not in st.session_state:
            st.session_state.user = None
        if "users_list" not in st.session_state:
            u1 = User("Jones", "jones@email.com", "1234")
            u2 = User("Peixoto", "peixoto@email.com", "5678")
            u3 = User("Miausculo", "miausculo@email.com", "gato")
            st.session_state.users_list = [u1, u2, u3]

    def login(self, email, password):
        logged_user = None
        for u in st.session_state.users_list:
            if email == u.get_email() and password == u.get_password():
                logged_user = u
                break
        if logged_user == None:
            st.error('Usuario ou senha invalidos')
            st.session_state.user = None
        else:
            st.success('Login feito!')
            st.session_state.user =logged_user
        

    