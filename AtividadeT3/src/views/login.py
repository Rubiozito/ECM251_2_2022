import streamlit as st 
from controllers.user_controller import UserController
import views.home_page as home
import time

def show_login_page():
    st.title("Bem vindo a lojihnha")

    st.header("Faça seu login")
    
    col1, col2 = st.columns([3,1])

    with col1:
        user = st.text_input(label='Digite seu nome de usuário:', placeholder = 'Usuário👽')
        senha = st.text_input(label='Digite sua senha:', placeholder = 'Senha🔐', type = 'password')

    def logar():
        if(UserController().tlogin(user, senha)):
            st.success("Logado com sucesso!")
            st.write('ok')
            home.show_home_page()
        else:
            st.error("Usuário ou senha inválidos😥")

    st.button(label = 'Entrar', help = 'Clique para entrar com sua conta', on_click = logar())

    with col2:
        st.image(image = "assets/logo_mel.png")
