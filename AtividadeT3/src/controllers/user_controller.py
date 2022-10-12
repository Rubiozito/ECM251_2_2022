import streamlit as st
from models.user import User

class UserController():
    def __init__(self):
        self.users_list = {
            "Jones": User(name="Jones", email= "jones@email.com", password= "1234"),
            "Peixoto": User(name="Peixoto", email= "peixoto@email.com", password= "5678"),
            "Miausculo": User(name="Miausculo", email= "miausculo@email.com", password= "gato"),
            "admin": User(name="admin", email= "admin@email.com", password= "admin")
        }

    def tlogin(self, name, password):
        return name in self.users_list and self.users_list[name].get_password() == password



        

    