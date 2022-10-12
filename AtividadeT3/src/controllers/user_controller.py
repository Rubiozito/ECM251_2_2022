import streamlit as st
from models.user import User

class UserController():
    def __init__(self):
        self.users_list = [
            User(name="Jones", email= "jones@email.com", password= "1234"),
            User(name="Peixoto", email= "peixoto@email.com", password= "5678"),
            User(name="Miausculo", email= "miausculo@email.com", password= "gato"),
            User(name="admin", email= "admin@email.com", password= "admin")
        ]

    def tlogin(self, name, password):
        user_try = User(name=name, password=password, email = None)
        for u in self.users_list:
            if u.get_name == user_try.get_name and u.get_password == user_try.get_password:
                return True
        return False


        

    