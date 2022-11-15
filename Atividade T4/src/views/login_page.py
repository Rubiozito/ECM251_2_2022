import streamlit as st
from controllers.user_controller import UserController
import time

def login_page():
    st.title("Bem vindo a lohjinha!")

    st.header("Faça seu login")

    col1, col2 = st.columns([3,1])

    with col1:
        email = st.text_input(label='Digite seu email:', placeholder = 'Email📧')
        senha = st.text_input(label='Digite sua senha:', placeholder = 'Senha🔐', type = 'password')


    def logar():
        if(UserController().login(email, senha)):
            time.sleep(1)
            st.session_state.page = 'home'
        else:
            st.error('Email ou senha incorretos')

    st.button(label='Entrar', help='Clique para entrar com a sua conta', on_click=logar)

    with col2:
        st.image(image = "assets/logo_mel.png")

        def go_to_cadastro():
            st.session_state.page = 'cadastro'

        st.write("Ainda não tem uma conta?")
        st.button(label='Cadastre-se', help='Clique para se cadastrar', on_click= go_to_cadastro)