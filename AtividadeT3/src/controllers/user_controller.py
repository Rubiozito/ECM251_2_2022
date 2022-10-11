import streamlit as st
from models.user import User

class UserController():
    def __init__(self):
        self.users_list = [
            User("Jones", "jones@email.com", "1234"),
            User("Peixoto", "peixoto@email.com", "5678"),
            User("Miausculo", "miausculo@email.com", "gato"),
            User("admin", "admin@email.com", "admin")
        ]

    def login(self, email, password):
        
        

    