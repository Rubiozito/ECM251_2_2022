import streamlit as st
from views.login_page import login_page
from views.home_page import home_page

class Sistema():
    
    def run():

        if 'page' not in st.session_state:
            st.session_state.page = 'login'

        if st.session_state.page == 'login':
            log.login_page()
        
        if st.session_state.page == 'home':
            home.home_page()
