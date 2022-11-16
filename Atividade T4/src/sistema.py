import streamlit as st
import views.login_page as log
import views.home_page as home
import views.new_user as cad
import views.edit_user as edit
import views.new_product as prod

class Sistema():
    
    def run():

        if 'cart' not in st.session_state:
            st.session_state.cart = []

        if 'log_user' not in st.session_state:
            st.session_state.log_user = None

        if 'page' not in st.session_state:
            st.session_state.page = 'login'

        if st.session_state.page == 'login':
            log.login_page()
        
        if st.session_state.page == 'home':
            home.home_page()

        if st.session_state.page == 'cadastro':
            cad.cadastro_page()

        if st.session_state.page == 'edit_user':
            edit.edit_user_page()

        if st.session_state.page == 'new_product':
            prod.new_product_page()