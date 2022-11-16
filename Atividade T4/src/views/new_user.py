import streamlit as st
from controllers.user_controller import UserController
from models.user import User

def cadastro_page():
    st.title("Bem vindo a lohjinha!")

    st.header("Faça seu cadastro")

    col1, col2 = st.columns([3,1])

    #não aceita email com @ e ponto, apenas letras e números, arrumar futuramente

    with col1:
        nome = st.text_input(label='Digite seu nome:', placeholder = 'Nome👤')
        email = st.text_input(label='Digite seu email:', placeholder = 'Email📧')
        senha = st.text_input(label='Digite sua senha:', placeholder = 'Senha🔐', type = 'password')
        confirmar_senha = st.text_input(label='Confirme sua senha:', placeholder = 'Senha🔐', type = 'password')
        new_user = User(nome, email, senha)

    def cadastrar():
        if(senha == confirmar_senha):
            if(UserController().insert_user(new_user)):
                st.success('Conta criada com sucesso')
            else:
                st.error('Email já cadastrado')
        else:
            st.error('Senhas não conferem')

    st.button(label='Cadastrar', help='Clique para cadastrar', on_click=cadastrar)

    with col2:
        st.image(image = "assets/logo_mel.png")
        
        def go_to_login():
            st.session_state.page = 'login'

        st.write("Já tem uma conta?")
        st.button(label='Faça seu login', help='Clique para fazer seu login', on_click= go_to_login)