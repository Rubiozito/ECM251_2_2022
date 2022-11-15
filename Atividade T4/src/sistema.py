import streamlit as st
import views.login_page as log
import views.home_page as home
import views.new_user as cad

class Sistema():
    
    def run():

        if 'page' not in st.session_state:
            st.session_state.page = 'login'

        if st.session_state.page == 'login':
            log.login_page()
        
        if st.session_state.page == 'home':
            home.home_page()

        if st.session_state.page == 'cadastro':
            cad.cadastro_page()
