import streamlit as st 
from controllers import UserController

def show_login_page():
    st.title("Bem vindo a lojihnha")

    st.header("Faça seu login")
    
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        user = st.text_input(label='Digite seu nome de usuário:', placeholder = 'Usuário👽')
        senha = st.text_input(label='Digite sua senha:', placeholder = 'Senha🔐', type = 'password')

    def logar():
        

