import streamlit as st 
from controllers.user_controller import UserController
from models.user import User

def edit_user_page():
    st.title("Atualize seus dados")

    col1, col2 = st.columns([3,1])

    with col1:
        st.write("Nome: " + st.session_state.log_user.name)
        new_name = st.text_input(label='Digite seu novo nome:', placeholder = 'Nome👤')
        def update_name():
            if(new_name != ''):
                st.session_state.log_user.set_name(new_name)
                new_user_name = User(new_name, st.session_state.log_user.email, st.session_state.log_user.password)
                UserController().update_user(new_user_name)
                st.success('Nome atualizado com sucesso')
            else:
                st.error('Digite um nome válido')
        st.button(label='Atualizar nome', help='Clique para atualizar seu nome', on_click=update_name)

        st.write("Email: " + st.session_state.log_user.email)
        new_email = st.text_input(label='Digite seu novo email:', placeholder = 'Email📧')
        def update_email():
            if(new_email != ''):
                st.session_state.log_user.set_email(new_email)
                new_user_email = User(st.session_state.log_user.name, new_email, st.session_state.log_user.password)
                UserController().update_user(new_user_email)
                st.success('Email atualizado com sucesso')
            else:
                st.error('Digite um email válido')
        st.button(label='Atualizar email', help='Clique para atualizar seu email', on_click=update_email)

        st.write("Senha: " + st.session_state.log_user.password)
        new_password = st.text_input(label='Digite sua nova senha:', placeholder = 'Senha🔐', type = 'password')
        confirm_new_password = st.text_input(label='Confirme sua nova senha:', placeholder = 'Senha🔐', type = 'password')
        def update_password():
            if(new_password == confirm_new_password):
                if(new_password != ''):
                    st.session_state.log_user.set_password(new_password)
                    new_user_password = User(st.session_state.log_user.name, st.session_state.log_user.email, new_password)
                    UserController().update_user(new_user_password)
                    st.success('Senha atualizada com sucesso')
                else:
                    st.error('Digite uma senha válida')
            else:
                st.error('Senhas não conferem')
        st.button(label='Atualizar senha', help='Clique para atualizar sua senha', on_click=update_password)


        def go_to_home():
            st.session_state.page = 'home'

        st.button(label='Voltar', help='Clique para voltar', on_click= go_to_home)